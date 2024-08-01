# Sql题解

## [1075. 项目员工 I](https://leetcode.cn/problems/project-employees-i/)(简单)

项目表 `Project`： 

```sql
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| project_id  | int     |
| employee_id | int     |
+-------------+---------+
主键为 (project_id, employee_id)。
employee_id 是员工表 Employee 表的外键。
```

员工表 `Employee`：

```
+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| employee_id      | int     |
| name             | varchar |
| experience_years | int     |
+------------------+---------+
主键是 employee_id。
```

请写一个 SQL 语句，查询每一个项目中员工的 **平均** 工作年限，**精确到小数点后两位**。

查询结果的格式如下：

```sql
Project 表：
+-------------+-------------+
| project_id  | employee_id |
+-------------+-------------+
| 1           | 1           |
| 1           | 2           |
| 1           | 3           |
| 2           | 1           |
| 2           | 4           |
+-------------+-------------+

Employee 表：
+-------------+--------+------------------+
| employee_id | name   | experience_years |
+-------------+--------+------------------+
| 1           | Khaled | 3                |
| 2           | Ali    | 2                |
| 3           | John   | 1                |
| 4           | Doe    | 2                |
+-------------+--------+------------------+

Result 表：
+-------------+---------------+
| project_id  | average_years |
+-------------+---------------+
| 1           | 2.00          |
| 2           | 2.50          |
+-------------+---------------+
第一个项目中，员工的平均工作年限是 (3 + 2 + 1) / 3 = 2.00；第二个项目中，员工的平均工作年限是 (3 + 2) / 2 = 2.50
```

我的题解:

```sql
select 
P.project_id as project_id, 
round(avg(E.experience_years),2) as average_years
from Project as p,Employee as E
where p.employee_id = E.employee_id
group by P.project_id
```

注意:题目要求保留两位小数，需要使用round函数来保留两位小数

最优题解:

```sql
SELECT
    project_id,
    ROUND(AVG(e.experience_years),2)  AS average_years
FROM
    Project as p 
LEFT JOIN
    Employee as e
ON
    p.employee_id = e.employee_id
GROUP BY
    p.project_id
```

## [175. 组合两个表](https://leetcode.cn/problems/combine-two-tables/)(简单)

表: `Person`

```sql
+-------------+---------+
| 列名         | 类型     |
+-------------+---------+
| PersonId    | int     |
| FirstName   | varchar |
| LastName    | varchar |
+-------------+---------+
personId 是该表的主键（具有唯一值的列）。
该表包含一些人的 ID 和他们的姓和名的信息。
```

表: `Address`

```sql
+-------------+---------+
| 列名         | 类型    |
+-------------+---------+
| AddressId   | int     |
| PersonId    | int     |
| City        | varchar |
| State       | varchar |
+-------------+---------+
addressId 是该表的主键（具有唯一值的列）。
该表的每一行都包含一个 ID = PersonId 的人的城市和州的信息。
```

编写解决方案，报告 `Person` 表中每个人的姓、名、城市和州。如果 `personId` 的地址不在 `Address` 表中，则报告为 `null` 。

以 **任意顺序** 返回结果表。

结果格式如下所示。

**示例 1:**

```sql
输入: 
Person表:
+----------+----------+-----------+
| personId | lastName | firstName |
+----------+----------+-----------+
| 1        | Wang     | Allen     |
| 2        | Alice    | Bob       |
+----------+----------+-----------+
Address表:
+-----------+----------+---------------+------------+
| addressId | personId | city          | state      |
+-----------+----------+---------------+------------+
| 1         | 2        | New York City | New York   |
| 2         | 3        | Leetcode      | California |
+-----------+----------+---------------+------------+
输出: 
+-----------+----------+---------------+----------+
| firstName | lastName | city          | state    |
+-----------+----------+---------------+----------+
| Allen     | Wang     | Null          | Null     |
| Bob       | Alice    | New York City | New York |
+-----------+----------+---------------+----------+
解释: 
地址表中没有 personId = 1 的地址，所以它们的城市和州返回 null。
addressId = 1 包含了 personId = 2 的地址信息。
```

我的题解:

```sql
select
p.firstName,
p.lastName,
a.city,
a.state
from 
Person as p
left join
Address as a
on a.personId = p.personId 
```

注意:两表为非对等表，并且不存在的返回null所以使用`left join`更好

最优题解:



## [1193. 每月交易 I](https://leetcode.cn/problems/monthly-transactions-i/)(中等)

表：`Transactions`

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| country       | varchar |
| state         | enum    |
| amount        | int     |
| trans_date    | date    |
+---------------+---------+
id 是这个表的主键。
该表包含有关传入事务的信息。
state 列类型为 ["approved", "declined"] 之一。
```

 

编写一个 sql 查询来查找每个月和每个国家/地区的事务数及其总金额、已批准的事务数及其总金额。

以 **任意顺序** 返回结果表。

查询结果格式如下所示。

 

**示例 1:**

```
输入：
Transactions table:
+------+---------+----------+--------+------------+
| id   | country | state    | amount | trans_date |
+------+---------+----------+--------+------------+
| 121  | US      | approved | 1000   | 2018-12-18 |
| 122  | US      | declined | 2000   | 2018-12-19 |
| 123  | US      | approved | 2000   | 2019-01-01 |
| 124  | DE      | approved | 2000   | 2019-01-07 |
+------+---------+----------+--------+------------+
输出：
+----------+---------+-------------+----------------+--------------------+-----------------------+
| month    | country | trans_count | approved_count | trans_total_amount | approved_total_amount |
+----------+---------+-------------+----------------+--------------------+-----------------------+
| 2018-12  | US      | 2           | 1              | 3000               | 1000                  |
| 2019-01  | US      | 1           | 1              | 2000               | 2000                  |
| 2019-01  | DE      | 1           | 1              | 2000               | 2000                  |
+----------+---------+-------------+----------------+--------------------+-----------------------+
```

==**注意:此题需要先对时间时间和国家分组，然后再通过再count和sum函数中添加条件来求解**==

我的题解:

```sql
# Write your MySQL query statement below
select 
date_format(t.trans_date,'%Y-%m') as month,
t.country,
count(t.id) as trans_count,
count(if(t.state='approved',1,null)) as approved_count,
sum(t.amount) as trans_total_amount,
sum(if(t.state = 'approved',t.amount,0)) as approved_total_amount
from Transactions as t
group by YEAR(t.trans_date)-MONTH(t.trans_date),t.country
```

最优题解:

```sql
select date_format(trans_date,"%Y-%m") month,country,
count(id) trans_count,# 总事务数
count(if(state="approved",amount,null)) approved_count, #批准事物数
sum(amount) trans_total_amount, # 总金额
sum(if(state="approved",amount,0)) approved_total_amount # 如果批准 则求总
from Transactions
group by month,country
```

## [1890. 2020年最后一次登录](https://leetcode.cn/problems/the-latest-login-in-2020/)(简单)

表: `Logins`

```
+----------------+----------+
| 列名           | 类型      |
+----------------+----------+
| user_id        | int      |
| time_stamp     | datetime |
+----------------+----------+
(user_id, time_stamp) 是这个表的主键(具有唯一值的列的组合)。
每一行包含的信息是user_id 这个用户的登录时间。
```

 

编写解决方案以获取在 `2020` 年登录过的所有用户的本年度 **最后一次** 登录时间。结果集 **不** 包含 `2020` 年没有登录过的用户。

返回的结果集可以按 **任意顺序** 排列。

返回结果格式如下例。

 

**示例 1:**

```
输入：
Logins 表:
+---------+---------------------+
| user_id | time_stamp          |
+---------+---------------------+
| 6       | 2020-06-30 15:06:07 |
| 6       | 2021-04-21 14:06:06 |
| 6       | 2019-03-07 00:18:15 |
| 8       | 2020-02-01 05:10:53 |
| 8       | 2020-12-30 00:46:50 |
| 2       | 2020-01-16 02:49:50 |
| 2       | 2019-08-25 07:59:08 |
| 14      | 2019-07-14 09:00:00 |
| 14      | 2021-01-06 11:59:59 |
+---------+---------------------+
输出：
+---------+---------------------+
| user_id | last_stamp          |
+---------+---------------------+
| 6       | 2020-06-30 15:06:07 |
| 8       | 2020-12-30 00:46:50 |
| 2       | 2020-01-16 02:49:50 |
+---------+---------------------+
解释：
6号用户登录了3次，但是在2020年仅有一次，所以结果集应包含此次登录。
8号用户在2020年登录了2次，一次在2月，一次在12月，所以，结果集应该包含12月的这次登录。
2号用户登录了2次，但是在2020年仅有一次，所以结果集应包含此次登录。
14号用户在2020年没有登录，所以结果集不应包含。
```

注意:此题需要以用户id分组并且还需要对时间进行max()来获得最后时间

我的题解:

```sql
select
l.user_id,
max(l.time_stamp) as last_stamp
from Logins as l
where year(l.time_stamp)  = '2020'
group by l.user_id
```

最优题解:

```sql
# Write your MySQL query statement below
select user_id,max(time_stamp) last_stamp from Logins where year(time_stamp)=2020 group by user_id;
```















# 算法题解

## [53. 最大子数组和](https://leetcode.cn/problems/maximum-subarray/)(中等)

给你一个整数数组 `nums` ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。**子数组**是数组中的一个连续部分。

**示例 1：**

```
输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
```

**示例 2：**

```
输入：nums = [1]
输出：1
```

**示例 3：**

```
输入：nums = [5,4,-1,7,8]
输出：23
```

 

**提示：**

- `1 <= nums.length <= 105`
- `-104 <= nums[i] <= 104`

 

**进阶：**如果你已经实现复杂度为 `O(n)` 的解法，尝试使用更为精妙的 **分治法** 求解。

使用动态规划解题:

第一步**思考每轮的决策，定义状态，从而得到 dp 表**

每一轮决策为数组nums[i]是否可以放在子数组中，放入和不放入状态i+1

所以状态为[i]对应的子问题:==**数组前i个数中子数组的最大和，记为dp[i]**==

第二步**找出最优子结构，进而推导出状态转移方程**

对于状态dp[i]是由dp[i-1]+nums[i-1]和nums[i]组成的
$$
dp[i] = max(dp[i-1]+nums[i-1],nums[i-1])
$$
第三步**确定边界条件和状态转移顺序**

此题dp长度为nums的len+1，dp[0]表示数组前0个数中的子数组最大和应该为0,既dp[0] = 0。状态应该由1开始一直到数组长度。

 我的题解:

```py
def maxNumber(nums: List[int]) -> int:
    dp = [0] * (len(nums) + 1)
    dp[1] = nums[0]
    m = dp[1]
    for i in range(2, len(nums) + 1):
        dp[i] = max(dp[i - 1] + nums[i - 1], nums[i - 1])
        if dp[i] > m:
            m = dp[i]

    return m
```

最优题解:

```py
    def maxSubArray(self, nums: List[int]) -> int:
        pre = 0  # 以某个数结尾的最大数组和
        max_nums = nums[0]  # 当前数组的最大子序和
        for num in nums:
            pre = max(pre + num, num)  # 不断迭代 pre 十分关键
            max_nums = max(max_nums, pre)
        return max_nums
```

相对于我的优化了空间复杂度。
