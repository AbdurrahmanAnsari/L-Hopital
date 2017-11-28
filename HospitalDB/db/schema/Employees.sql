-- Table: patients

-- DROP TABLE employees;

CREATE TABLE employees
(
    "Employee_ID" bigint        NOT NULL,
    "E_F_Name"     text,
    "E_L_Name"     text,
    "E_Age"        bigint,
    "E_Gender"     text,
    "E_Address"    text,
    "E_Position"   text,
    CONSTRAINT employee_pkey PRIMARY KEY ("Employee_ID")
)
WITH (
  OIDS=FALSE
);