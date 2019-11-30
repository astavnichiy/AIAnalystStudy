-- 1. ������� ������, � ������� �� ������� ��� ������ � ������ � ������, ������.

SELECT * 
FROM geodata._cities c
INNER JOIN geodata._regions d ON c.region_id = d.id
INNER JOIN geodata._countries cr ON c.country_id = cr.id;

-- 2. ������� ��� ������ �� ���������� �������.
SELECT distinct title_ru
FROM geodata._cities c
WHERE region_id in (SELECT id FROM geodata._regions
where title_ru = '���������� �������');

-- 1. ������� ������� �������� �� �������. 
SELECT avg(s.salary),
d.dept_no FROM
employees.salaries s,
(SELECT `dept_emp`.`emp_no`,
    `dept_emp`.`dept_no`,
    `dept_emp`.`from_date`,
    `dept_emp`.`to_date`
FROM `employees`.`dept_emp`
union all
SELECT `dept_manager`.`dept_no`,
    `dept_manager`.`emp_no`,
    `dept_manager`.`from_date`,
    `dept_manager`.`to_date`
FROM `employees`.`dept_manager`) as d
Where 1=1
and s.to_date > sysdate()
and s.`emp_no` = d.`emp_no`
GROUP BY d.dept_no

--2. ������� ������������ �������� � ����������. 
SELECT max(s.salary),
d.emp_no FROM
employees.salaries s,
(SELECT `dept_emp`.`emp_no`,
    `dept_emp`.`dept_no`,
    `dept_emp`.`from_date`,
    `dept_emp`.`to_date`
FROM `employees`.`dept_emp`
union all
SELECT `dept_manager`.`dept_no`,
    `dept_manager`.`emp_no`,
    `dept_manager`.`from_date`,
    `dept_manager`.`to_date`
FROM `employees`.`dept_manager`) as d
Where 1=1
and s.to_date > sysdate()
and s.`emp_no` = d.`emp_no`
GROUP BY d.emp_no



--3. ������� ������ ����������, � �������� ������������ ��������.
Delete from employees.`employees` 
Where e.emp_no in (SELECT emp_no FROM employees.salaries ORDER BY salary DESC LIMIT 1)

--4. ��������� ���������� ����������� �� ���� �������.
select d.dept_no, count(emp_no) from
(SELECT `dept_emp`.`dept_no`,
    `dept_emp`.`emp_no`,
    `dept_emp`.`from_date`,
    `dept_emp`.`to_date`
FROM `employees`.`dept_emp`
union all
SELECT `dept_manager`.`dept_no`,
    `dept_manager`.`emp_no`,
    `dept_manager`.`from_date`,
    `dept_manager`.`to_date`
FROM `employees`.`dept_manager`) as d
Where to_date > sysdate()
group by d.dept_no 


--5. ����� ���������� ����������� � ������� � ����������, ������� ����� ����� �������� �����.
select res.dept_no, 
count(res.emp_no), 
sum(res.salary)
from
(SELECT d.`dept_no`,
    d.`emp_no`,
    d.`from_date`,
    d.`to_date`,
    s.salary
FROM `employees`.`dept_emp` d, `employees`.`salaries` s
Where d.emp_no = s.emp_no
and s.`to_date` > sysdate()
and d.`to_date` > sysdate()  
union all
SELECT d.`dept_no`,
    d.`emp_no`,
    d.`from_date`,
    d.`to_date`,
    s.salary
FROM `employees`.`dept_manager` d, `employees`.`salaries` s
Where d.emp_no = s.emp_no
and s.`to_date` > sysdate()
and d.`to_date` > sysdate()
) as res
group by res.dept_no 

