-- Table: patients

-- DROP TABLE patients;

CREATE TABLE departments
(
    "Department_ID"       bigint        NOT NULL,
    "Department_Name"     text,
    CONSTRAINT department_pkey PRIMARY KEY ("Department_ID"),
)
WITH (
  OIDS=FALSE
);
