SET SEARCH_PATH TO district_ms;

--Que 1
select *
from complaints;

--Que 2
SELECT cp_id, cp_issue
FROM complaints;

--Que 3
SELECT *
FROM complaints
WHERE c_id=171;

--Que 4
SELECT Td_id, T_name
FROM Tehsil;

-- Que 5
SELECT *
FROM citizens
ORDER BY c_id ASC ;

--Que 6
SELECT L_id, L_name, Td_id
FROM law_enforcement_agency;

--Ques7
SELECT c_dob
FROM citizens
where c_dob > '1990-01-01'

--Que 8
select *
from issue;

--Que 9
SELECT * 
From status
where ts_duration > 7
order by ts_duration asc;

-- Que 10
select f_rating, f_review
from feedback
where f_rating < 7
order by f_rating;

-- Que 11
CREATE OR REPLACE FUNCTION Issues()
	-- declaring return type
	RETURNS integer
	LANGUAGE 'plpgsql'
	
	AS $BODY$
	
	DECLARE
	entries integer;
	BEGIN
	select count(*)
	into entries
	from complaints
    inner join status
	on complaints.cp_id = status.cp_id
	where ts_duration > 7;
	
	return entries;
	END;
	$BODY$;

select * from Issues();

-- Que 12
select *
from complaints
where td_id = 2 or td_id = 5;

-- Que 13
SELECT t_id, t_name, tehsildars.td_id, td_name, td_contact_no, s_zone
FROM tehsildars
INNER JOIN tehsil
ON tehsildars.td_id = tehsil.td_id;

-- Que 14
SELECT citizens.c_id, c_name, c_contact_no, c_address, c_dob, cp_id, cp_issue
FROM complaints
INNER JOIN citizens
ON complaints.c_id = citizens.c_id
order by c_dob;

-- Que 15
SELECT cp_id, c_id, complaints.td_id, cp_issue, l_name, l_helpline_no
FROM complaints
INNER JOIN law_enforcement_agency
ON complaints.l_id = law_enforcement_agency.l_id;

-- Que 16
create view view_complaints as
select cp_issue, cp_location, td_id, l_id, cp_registration_date
from complaints
where cp_registration_date < '2022-10-01';

select *
from view_complaints;

-- Que 17
create view view_issue as
select r_reason, r_reopen_date, cp_id
from issue
where r_reopen_date < '2022-10-01';

SELECT cp_issue, cp_location, td_id, l_id, cp_registration_date, r_reason, r_reopen_date
FROM complaints
INNER JOIN view_issue
ON complaints.cp_id = view_issue.cp_id
order by r_reopen_date;

-- Que 18
create view view_feedback as
select f_rating, f_review, cp_id
from feedback
where f_rating < 7;

SELECT cp_issue, cp_location, td_id, l_id, cp_registration_date, f_rating, f_review
FROM complaints
INNER JOIN view_feedback
ON complaints.cp_id = view_feedback.cp_id
order by f_rating;

-- Que 19
create view view_status as
select ts_status, ts_duration, cp_id
from status
where ts_status = 'Work In Progress';

SELECT cp_issue, cp_location, td_id, l_id, cp_registration_date, ts_status, ts_duration
FROM complaints
INNER JOIN view_status
ON complaints.cp_id = view_status.cp_id;

-- Que 20
create or replace function "trig_func1"()
returns TRIGGER
LANGUAGE 'plpgsql'
as $body$
declare cit_id integer;
declare issue text;
BEGIN
select c_id, cp_issue into cit_id, issue
from complaints
where c_id = new.c_id and cp_issue = new.cp_issue;
if(cit_id = new.c_id and issue = new.cp_issue) then
raise notice 'complaint already exists, if you wish you can reopen the complaint.';
ELSE
raise notice 'complaint does not exist.';
return new;
end if;
end
$body$;

CREATE TRIGGER "check_duplication"
before insert
ON complaints
FOR EACH ROW
EXECUTE PROCEDURE trig_func1();

INSERT INTO complaints values(1041, 'Water leakage from the pipes', '2022-11-23', 'No.4, Brooks Villa, Nebraska', 194, 2, 8);