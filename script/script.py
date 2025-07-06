import argparse
import configparser
import os
import re

from joblib.testing import param


def get_config(cig, section, key, is_list=False):
    line = cig.get(section, key)
    # 去除line中的注释和空格
    line = line.split('#')[0].strip()
    return line if not is_list else line.split(',')


def get_absolute_path(path):
    # 获取绝对路径
    return os.path.abspath(path)


def get_files(path):
    # 获取路径下的所有子文件路径
    return [get_absolute_path(os.path.join(path, file)) for file in os.listdir(path)]


def get_file_name(path):
    # 获取文件名
    return os.path.basename(path)


def get_suffix(path):
    # 获取文件后缀
    return os.path.splitext(path)[-1]


def get_path_by_suffix(path, suffixes):
    # 如果文件名称带有前缀.跳过
    if get_file_name(path).startswith('.'):
        return []
    # 获取指定后缀的文件路径
    path_list = []
    for p in get_files(path):
        # 文件夹递归调用
        if os.path.isdir(p):
            path_list.extend(get_path_by_suffix(p, suffixes))
        # 判断文件后缀是否在后缀列表中
        elif get_suffix(p) in suffixes:
            path_list.append(p)
    return path_list


def get_link(md_path):
    link_path = []
    pattern = r'!\[.*?\]\((.+?)\)'
    pattern += r'|<img.*?src="(.*?)".*?>'
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
        matches = re.findall(pattern, content, re.IGNORECASE)
        for match in matches:
            # 每个 match 是一个元组，两个分组中只有一个有内容
            link = match[0] if match[0] else match[1]
            if not link:
                continue
            local_path = os.path.join(os.path.dirname(md_path), link)
            # 判断link是否是本地文件
            if os.path.exists(local_path):
                link_path.append(get_absolute_path(local_path))
    return link_path


if __name__ == '__main__':
    # 获取配置
    config = configparser.ConfigParser()
    config.read('config.properties', encoding='utf-8')
    root_path = get_absolute_path(get_config(config, 'DEFAULT', 'root.path'))
    root_suffix = get_config(config, 'DEFAULT', 'root.suffix', True)
    print(f"文件根路径:{root_path}\n后缀列表:{root_suffix}")
    # 获取全部后缀在root_suffix中的文件路径
    need_clear_file = get_path_by_suffix(root_path, root_suffix)
    print(f"所有需要清理的文件:{need_clear_file}")
    # 获得全部md文档路径
    md_file = get_path_by_suffix(root_path, ['.md'])
    print(f"所有md文件:{md_file}")
    not_clear_file = []
    for md in md_file:
        # 获取md文档中的所有链接
        links = get_link(md)
        print(f"{md}中的链接:{links}")
        not_clear_file.extend(links)
    final_need_clear_file = list(set(need_clear_file) - set(not_clear_file))
    print(f"需要清理的文件:{final_need_clear_file},数量为:{len(final_need_clear_file)}")
    size = 0
    for file in final_need_clear_file:
        size += os.path.getsize(file)
        os.remove(file)
    print(f"清理完成,清理了约{(size / 1024):.2f}KB的文件")