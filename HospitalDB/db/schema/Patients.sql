-- Table: patients

-- DROP TABLE patients;

CREATE TABLE patients
(
    "Patient_ID" bigint        NOT NULL,
    "P_F_Name"     text,
    "P_L_Name"     text,
    "P_Age"        bigint,
    "P_Gender"     text,
    "P_Address"    text,
    "P_Department" bigint,
    "P_Room"       bigint,
    CONSTRAINT patient_pkey PRIMARY KEY ("Patient_ID"),
    CONSTRAINT patient_fkey FOREIGN KEY ("P_Department") REFERENCES "departments" ("Department_ID") ON UPDATE CASCADE,
    CONSTRAINT patient_fkey2 FOREIGN KEY ("P_Room") REFERENCES "rooms" ("Room_Number") ON UPDATE CASCADE
)
WITH (
  OIDS=FALSE
);
