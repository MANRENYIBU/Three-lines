

# 结构化提示词

资料来源:[⭐ 结构化提示词 - 飞书云文档](https://langgptai.feishu.cn/wiki/RXdbwRyASiShtDky381ciwFEnpe)

## 1、什么是结构化 Prompt ？

结构化的思想很普遍，结构化内容也很普遍，我们日常写作的文章，看到的书籍都在使用标题、子标题、段落、句子等语法结构。**结构化 Prompt 的思想通俗点来说就是像写文章一样写 Prompt。**

为了阅读、表达的方便，我们日常有各种写作的模板，用来控制内容的组织呈现形式。例如古代的八股文、现代的简历模板、学生实验报告模板、论文模板等等模板。所以结构化编写 Prompt 自然也有各种各样优质的模板帮助你把 Prompt 写的更轻松、性能更好。所以写**结构化 Prompt 可以有各种各样的模板，你可以像用 PPT 模板一样选择或创造自己喜欢的模板**。

在这之前，虽然也有类似结构化思想，但是更多体现在思维上，缺乏在 prompt 上的具体体现。

例如知名的 CRISPE 框架([3])，CRISPE 分别代表以下含义：

- CR：Capacity and Role（能力与角色）。你希望 ChatGPT 扮演怎样的角色。
- I：Insight（洞察力），背景信息和上下文（坦率说来我觉得用 Context 更好）。
- S：Statement（指令），你希望 ChatGPT 做什么。
- P：Personality（个性），你希望 ChatGPT 以什么风格或方式回答你。
- E：Experiment（尝试），要求 ChatGPT 为你提供多个答案。

**最终写出来的 Prompt 是这样的：**

```Plaintext
Act as an expert on software development on the topic of machine learning frameworks, and an expert blog writer. The audience for this blog is technical professionals who are interested in learning about the latest advancements in machine learning. Provide a comprehensive overview of the most popular machine learning frameworks, including their strengths and weaknesses. Include real-life examples and case studies to illustrate how these frameworks have been successfully used in various industries. When responding, use a mix of the writing styles of Andrej Karpathy, Francois Chollet, Jeremy Howard, and Yann LeCun.
```

这类思维框架只呈现了 Prompt 的内容框架，但没有提供模板化、结构化的 prompt 形式。

**而我们所提倡的结构化、模板化 Prompt，写出来是这样的**

> 该示例来自 LangGPT 项目: https://github.com/yzfly/LangGPT/blob/main/README_zh.md

```Plaintext
# Role: 诗人

## Profile

- Author: YZFly
- Version: 0.1
- Language: 中文
- Description: 诗人是创作诗歌的艺术家，擅长通过诗歌来表达情感、描绘景象、讲述故事，具有丰富的想象力和对文字的独特驾驭能力。诗人创作的作品可以是纪事性的，描述人物或故事，如荷马的史诗；也可以是比喻性的，隐含多种解读的可能，如但丁的《神曲》、歌德的《浮士德》。

### 擅长写现代诗
1. 现代诗形式自由，意涵丰富，意象经营重于修辞运用，是心灵的映现
2. 更加强调自由开放和直率陈述与进行“可感与不可感之间”的沟通。

### 擅长写七言律诗
1. 七言体是古代诗歌体裁
2. 全篇每句七字或以七字句为主的诗体
3. 它起于汉族民间歌谣

### 擅长写五言诗
1. 全篇由五字句构成的诗
2. 能够更灵活细致地抒情和叙事
3. 在音节上，奇偶相配，富于音乐美

## Rules
1. 内容健康，积极向上
2. 七言律诗和五言诗要押韵

## Workflow
1. 让用户以 "形式：[], 主题：[]" 的方式指定诗歌形式，主题。
2. 针对用户给定的主题，创作诗歌，包括题目和诗句。

## Initialization
作为角色 <Role>, 严格遵守 <Rules>, 使用默认 <Language> 与用户对话，友好的欢迎用户。然后介绍自己，并告诉用户 <Workflow>。
```

**基于上述** **`诗人`** **prompt 例子，说明结构化 prompt 的几个概念：**

- **标识符**：`#`, `<>` 等符号(`-`, `[]`也是)，这两个符号依次标识`标题`,`变量`，控制内容层级，用于标识层次结构。
- **属性词**：`Role`, `Profile`, `Initialization` 等等，属性词包含语义，是对模块下内容的总结和提示，用于标识语义结构。

 日常的文章结构是通过字号大小、颜色、字体等样式来标识的，ChatGPT 接收的输入没有样式，因此借鉴 markdown，yaml 这类标记语言的方法或者 json 这类数据结构实现 prompt 的结构表达都可以，例如用标识符 `#` 标识一级标题，`##`标识二级标题，以此类推。**尤其是使用 json， yaml 这类成熟的数据结构，对 prompt 进行工程化开发特别友好。**  LangGPT 目前选用的是 Markdown 标记语法，一是因为 ChatGPT 网页版本身就支持 Markdown 格式，二是希望对非程序员朋友使用更加友好。程序员朋友推荐使用yaml, json 等进行结构化 prompt 开发。

 `属性词`好理解，和学术论文中使用的`摘要`，`方法`，`实验`，`结论`的段落标题起的作用一样。

 `标识符`，`属性词`都是可替换的，可以替换为你喜欢的符号和内容。

 结构化 prompt 直观上和传统的 prompt 方式差异就很大，那么为什么提倡结构化方式编写 Prompt 呢？

## 2、结构化 Prompt 的优势

优势太多了，说一千道一万，**归根结底还是结构化、模板化 Prompt 的性能好！**

这一点已经在许多朋友的日常使用甚至商业应用中得到证明。许多企业，乃至网易、字节这样的互联网大厂都在使用结构化 Prompt！

此外结构化、模板化 Prompt 还有许多优势，**这些优势某种意义上又是其在实际使用时表现卓越的原因。**

### 2.1 优势一：层级结构：内容与形式统一

#### 2.1.1 结构清晰，可读性好

结构化方式编写出来的 Prompt 层级结构十分清晰，将结构在形式上和内容上统一了起来，**可读性很好**。

- `Role (角色)` 作为 Prompt 标题统摄全局内容。
- `Profile (简介)`、`Rules（规则）` 作为二级标题统摄相应的局部内容。
- `Language`、`Description` 作为关键词统摄相应句子、段落。

#### 2.1.2 结构丰富，表达性好

CRISPE 这类框架命中注定结构简单，因为过于复杂将难以记忆，大大降低实操性，因此其往往只有一层结构，这限制了 Prompt 的表达。

结构化 prompt 的结构由形式控制，完全没有记忆负担。只要模型能力支持，可以做到二层，三层等更多、更丰富的层级结构。

那么为什么要用更丰富的结构？这么做有什么好处呢？

这种方式写出来的 Prompt **符合人类的表达习惯**，与我们日常写文章时有标题、段落、副标题、子段落等丰富的层级结构是一样的。

这种方式写出来的 Prompt **符合** **ChatGPT** **的认知习惯**，因为 ChatGPT 正是在大量的文章、书籍中训练得到，其训练内容的层级结构本来就是十分丰富的。

### 2.2 优势二：提升语义认知

结构化表达同时降低了人和 GPT 模型的认知负担，**大大提高了人和GPT模型对 prompt 的语义认知。** 对人来说，Prompt 内容一目了然，语义清晰，只需要依样画瓢写 Prompt 就行。如果使用 LangGPT 提供的 Prompt 生成助手，还可以帮你生成高质量的初版 Prompt。

> 使用 LangGPT 生成提示词：
>
> 1. 月之暗面 Kimi × LangGPT 提示词专家: https://kimi.moonshot.cn/kimiplus/conpg00t7lagbbsfqkq0
> 2. OpenAI 商店 LangGPT 提示词专家：https://chatgpt.com/g/g-Apzuylaqk-langgpt-ti-shi-ci-zhuan-jia

生成的初版 Prompt 足以应对大部分日常场景，生产级应用场景下的 prompt 也可以在这个初版 prompt 基础上进行迭代优化得到，能够大大降低编写 prompt 的任务量。

对 GPT 模型来说，**标识符标识的层级结构实现了聚拢相同语义，梳理语义的作用，降低了模型对 Prompt 的理解难度**，便于模型理解 prompt 语义。

**属性词实现了对 prompt 内容的语义提示和归纳作用，缓解了 Prompt 中不当内容的干扰。** 使用属性词与 prompt 内容相结合，实现了局部的总分结构，便于模型提纲挈领的获得 prompt 整体语义。

### 2.3 优势三：定向唤醒大模型深度能力

**使用特定的属性词能够确保定向唤醒模型的深层能力。**

实践发现让模型扮演某个角色其能大大提高模型表现，所以一级标题设置的就是 `Role`（角色） 属性词，直接将 Prompt 固定为角色，确保定向唤醒模型的角色扮演能力。也可使用 `Expert`（专家）, `Master`(大师)等提示词替代 `Role`，将 Prompt 固定为某一领域专家。

再比如 `Rules`，规定了模型必须尽力去遵守的规则。比如在这里添加不准胡说八道的规则，缓解大模型幻觉问题。添加输出内容必须积极健康的规则，缓解模型输出不良内容等。用 `Constraints`(约束)，中文的 `规则` 等词替代也可。

下面是示例 Prompt 中使用到的一些属性词介绍：

```Plaintext
# Role: 设置角色名称，一级标题，作用范围为全局

## Profile: 设置角色简介，二级标题，作用范围为段落

- Author: yzfly    设置 Prompt 作者名，保护 Prompt 原作权益
- Version: 1.0     设置 Prompt 版本号，记录迭代版本
- Language: 中文   设置语言，中文还是 English
- Description:     一两句话简要描述角色设定，背景，技能等

### Skill:  设置技能，下面分点仔细描述
1. xxx
2. xxx


## Rules        设置规则，下面分点描述细节
1. xxx
2. xxx

## Workflow     设置工作流程，如何和用户交流，交互
1. 让用户以 "形式：[], 主题：[]" 的方式指定诗歌形式，主题。
2. 针对用户给定的主题，创作诗歌，包括题目和诗句。

## Initialization  设置初始化步骤，强调 prompt 各内容之间的作用和联系，定义初始化行为。
作为角色 <Role>, 严格遵守 <Rules>, 使用默认 <Language> 与用户对话，友好的欢迎用户。然后介绍自己，并告诉用户 <Workflow>。
```

好的属性词也很关键，你可以定义、添加、修改自己的属性词。

### 2.4 优势四：像代码开发一样构建生产级 Prompt

代码是调用机器能力的工具， Prompt 是调用大模型能力的工具。**Prompt 越来越像新时代的编程语言。** 这一观点我在之前的文章中也提过，并获得了许多朋友的认同。

在生产级 AIGC 应用的开发中，**结构化 prompt 使得 prompt 的开发也像代码开发一样有规范。** 结构化 Prompt 的规范可以多种多样，用 json，yaml 实现都可以，GitHub 用户 ZhangHanDong([4]) 甚至还专门为 Prompt 设计了描述语言 prompt-description-language([5])。

**结构化 Prompt 的这些规范，这些模块化设计，能够大大便利于 prompt 后续的维护升级，便利于多人协同开发设计。** 这一点程序员群体应该深有感受。

想象一下，你是某公司一名 prompt 工程师，某一个或多个 prompt 因为某些原因（前任离职或调岗）需要你负责维护升级，你是更喜欢面对结构化的 Prompt 还是非结构化的 Prompt 呢？结构化 Prompt 是`自带使用文档` 的，十分清晰明了。

再比如要设计的应用是由许多 `agents` （由不同的 prompt 调用大模型能力实现）构建的 `chain` 实现的，当团队一起开发这个应用，每个人都负责某一 `agents` 的开发，上下游之间如何协同呢？数据接口如何定义呢？采用结构化模块化设计只需要在 prompt 里添加 `Input` (输入)和 `Output`（输出）模块，告诉大模型接收的输入是怎样的，需要以怎样的方式输出即可，十分便利。固定输入输出后，各开发人员完成自己的 agent 开发工作即可。

**像复用代码一样复用 Prompt。** 对于某些常用的模块，比如 `Rules` 是不是可以像复用代码一样实现 Prompt 的复用？是不是可以像面向对象的编程一样复用某些基础角色？LangGPT 提供的 Prompt 生成助手某种意义上就是自动化的实现了基础角色的复用。

同时 Prompt 作为一种文本，也完全可以使用 Git 等工具像管理代码一样对 prompt 进行版本管理。

## 3、如何写好结构化 Prompt ?

当我们在谈 Prompt 的结构的时候，我们在谈什么？

当我们构建结构化 Prompt 的时候，我们在构建什么？什么是真正重要的事情？

### 3.1 构建全局思维链

对大模型的 Prompt 应用CoT 思维链方法的有效性是被研究和实践广泛证明了的。

**一个好的结构化 Prompt 模板，某种意义上是构建了一个好的全局思维链。** 如 LangGPT 中展示的模板设计时就考虑了如下思维链:

> Role (角色) -> Profile（角色简介）—> Profile 下的 skill (角色技能) -> Rules (角色要遵守的规则) -> Workflow (满足上述条件的角色的工作流程) -> Initialization (进行正式开始工作的初始化准备) -> 开始实际使用

一个好的 Prompt ，内容结构上最好也是逻辑清晰连贯的。**结构化 prompt 方法将久经考验的逻辑思维链路融入了结构中，大大降低了思维链路的构建难度。**

构建 Prompt 时，不妨参考优质模板的全局思维链路，熟练掌握后，完全可以对其进行增删改留调整得到一个适合自己使用的模板。例如当你需要控制输出格式，尤其是需要格式化输出时，完全可以增加 `Output` 或者 `OutputFormat` 这样的模块（可参考附录中的 AutoGPT 模板）。

### 3.2 保持上下文语义一致性

包含两个方面，一个是**格式语义一致性**，一个是**内容语义一致性**。

**格式语义一致性是指标识符的标识功能前后一致。** 最好不要混用，比如 `#` 既用于标识标题，又用于标识变量这种行为就造成了前后不一致，这会对模型识别 Prompt 的层级结构造成干扰。

**内容语义一致性是指思维链路上的属性词语义合适。** 例如 LangGPT 中的 `Profile` 属性词，原来是 Features，但实践+思考后我更换为了 `Profile`，使之功能更加明确：即角色的简历。结构化 Prompt 思想被诸多朋友广泛使用后衍生出了许许多多的模板，但基本都保留了 `Profile` 的诸多设计，说明其设计是成功有效的。

为什么前期会用 Features 呢？因为 LangGPT 的结构化思想有受到 AI-Tutor([7]) 项目很大启发，而 AI-Tutor 项目中并无 `Profile` 一说，与之功能近似的是 `Features`。但 AI-Tutor 项目中的提示词过于复杂，并不通用。为形成一套简单有效且通用的 Prompt 构建方法，我参考 AutoGPT 中的提示词，结合自己对 Prompt 的理解，提出了 LangGPT 中的结构化思想，重新设计了并构建了 LangGPT 中的结构化模板。

**内容语义一致性还包括属性词和相应模块内容的语义一致。** 例如 `Rules` 部分是角色需要遵守规则，则不宜将角色技能、描述大量堆砌在此。

### 3.3 有机结合其他 Prompt 技巧

结构化 Prompt 编写思想是一种方法，与其他例如 CoT, ToT, Think step by step 等技巧和方法并不冲突，构建高质量 Prompt 时，将这些方法结合使用，结构化方式能够更便于各个技巧间的协同组织，例如 刘海同学([8]) 就将 CoT 方法融合到结构化 Prompt 中编写提示词。

从 prompting 的角度有哪些方法可以提高大模型在复杂任务上的性能表现呢？

汇总现有的一些方法：

1. 细节法：给出更清晰的指令，包含更多具体的细节
2. 分解法：将复杂的任务分解为更简单的子任务 （Let's think step by step, CoT，LangChain等思想）
3. 记忆法：构建指令使模型时刻记住任务，确保不偏离任务解决路径（system 级 prompt）
4. 解释法：让模型在回答之前进行解释，说明理由 （CoT 等方法）
5. 投票法：让模型给出多个结果，然后使用模型选择最佳结果 （ToT 等方法）
6. 示例法：提供一个或多个具体例子，提供输入输出示例 （one-shot, few-shot 等方法）

上面这些方法最好结合使用，以实现在复杂任务中实现使用不可靠工具（LLMs）构建可靠系统的目标。

> 原文：https://www.zhihu.com/pin/1661516375779852288

## 4、结构化 Prompt 对不同模型的适用性

不同模型的能力维度不同，从最大化模型性能的角度出发，有必要针对性开发相应的 Prompt。对一些基础简单的 Prompt 来说（比如只有一两句话的 prompt），可能在不同模型上表现差不多，但是任务难度变复杂，prompt 也相应的复杂以后，不同模型表现则会出现明显分化。结构化 prompt 方法也是如此。

结构化 Prompt 编写对模型基础能力有一定要求，要求模型本身具有较好的指令遵循、结构识别分析能力。从实践来看，GPT-4 是最佳选择， Claude 模型能力次之， GPT-3.5 勉强可用。依据笔者实践和身边朋友使用的反馈来看，在 GPT-4 和 Claude 模型上的表现情况都不错， GPT-3.5 则存在表现不稳定现象。

对于其他模型，由于模型本身能力较弱，笔者实际使用很少，若有兴趣欢迎向笔者反馈结构化 Prompt 在这些模型上的表现情况。

若有条件，推荐使用 GPT-4 。出于节约成本和服务可访问性的考虑，可能许多朋友需要使用 GPT-3.5 模型。由于 GPT-3.5 模型性能较弱，当你发现结构化 Prompt 在 GPT-3.5 表现不佳时，可以考虑`降低结构复杂度`、`调整属性词`、`迭代修改 Prompt`。例如 LangGPT 助手的 GPT-3.5 版本（如下），就将原本的多级结构降维为二级结构（1. 2. 3. 为一级，- 为二级），同时参考 AutoGPT 中的提示词使用了 `4.Goals`, `5.Constraints` 等属性词。同时，依据 prompt 表现，不断修改调优你的提示词。

总之，在模型能力允许的情况下，结构化确实能提高 Prompt 性能，但是在不符合你的实际需要时，仍然需要使用各种方法调试修改 Prompt。

> 来源：https://raw.githubusercontent.com/yzfly/LangGPT/main/LangGPT/ChatGPT3.5.txt

```Plaintext
1.Expert: LangGPT
2.Profile:
- Author: YZFly
- Version: 1.0
- Language: English
- Description: Your are {{Expert}} which help people write wonderful and powerful prompt.
3.Skills:
- Proficiency in the essence of LangGPT structured prompts.
- Write powerful LangGPT prompts to maximize ChatGPT performance.
4.LangGPT Prompt Example:
{{
1.Expert: {expert name}
2.Profile:
- Author: YZFly
- Version: 1.0
- Language: English
- Description: Describe your expert. Give an overview of the expert's characteristics and skills
3.Skills:
- {{ skill 1 }}
- {{ skill 2 }}
4.Goals:
- {{goal 1}}
- {{goal 2}}
5.Constraints:
- {{constraint 1}}
- {{constraint 2}}
6.Init: 
- {{setting 1}}
- {{setting 2}}
}}
5.Goals:
- Help write powerful LangGPT prompts to maximize ChatGPT performance.
- Output the result as markdown code.

6.Constraints:
- Don't break character under any circumstance.
- Don't talk nonsense and make up facts.
- You are {{Role}}, {{Role Description}}. 
- You will strictly follow {{Constraints}}.
- You will try your best to accomplish {{Goals}}.

7.Init: 
- Ask user to input [Prompt Usage].
- Help user make write powerful LangGPT prompts based on [Prompt Usage].
```

## 5、结构化 Prompt 的开发工作流

日常使用时，直接问 ChatGPT 效果可以的话，直接问就行。

构建复杂高性能结构化 Prompt 有以下几种工作流：

1. 自动化生成初版结构化 Prompt -> 手工迭代调优 -> 符合需求的 prompt (推荐)
2. 自动化生成初版结构化 Prompt -> 自动化分析评估 Prompt -> 基于评估结果迭代调优 -> 符合需求的 prompt （推荐）
3. 手工套用现有模板 —> 手工迭代调优 -> 符合需求的 prompt

1, 2 较为推荐，能够大大降低工作量，大佬请随意。

自动化生成初版结构化 Prompt 推荐使用 **LangGPT([9])**，使用其他 Prompt 生成方法也可。

> 使用 LangGPT 生成提示词：
>
> 1. 月之暗面 Kimi × LangGPT 提示词专家: https://kimi.moonshot.cn/kimiplus/conpg00t7lagbbsfqkq0
> 2. OpenAI 商店 LangGPT 提示词专家：https://chatgpt.com/g/g-Apzuylaqk-langgpt-ti-shi-ci-zhuan-jia

自动化分析评估 Prompt 可以使用 prompt 评分分析类 Prompt，可参考 LangGPT 群精选——Prompt 优化([10])。中的高质量 Prompt。

## 6、结构化 Prompt 的局限性

结构化 Prompt 依赖于基座模型能力，并不能解决模型本身的问题，结构化 Prompt 并不能突破大模型 Prompt 方法本身的局限性。

已知的无法解决的问题：

- 大模型本身的幻觉问题
- 大模型本身知识老旧问题
- 大模型的数学推理能力弱问题 (解数学问题)
- 大模型的视觉能力弱问题(构建 SVG 矢量图等场景)
- 大模型字数统计问题（不论是字符数和 token 数，大模型都无法统计准确。需要输出指定字数时，将数值设定的高一些，后期自己调整一下，比如希望他输出100字文案，告诉他输出150字。）
- 同一 Prompt 在不同模型间的性能差异问题
- 其他已知问题等

可参考：构建生产级鲁棒高性能 Prompt([11])
