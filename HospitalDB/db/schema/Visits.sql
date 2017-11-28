-- Table: patients

-- DROP TABLE visits;

CREATE TABLE visits
(
    "Visit_ID"     bigint        NOT NULL,
    "Admitted"     text,
    "Discharged"   text,
    "V_Deparment"  bigint,
    "Reason_For_Visit"     text,
    "Diagnosis"    text,
    "Preescription" bigint,
    "Notes"       text,
    "Room"        text,
    CONSTRAINT visit_pkey PRIMARY KEY ("Visit_ID"),
    CONSTRAINT visit_fkey FOREIGN KEY ("V_Department") REFERENCES "departments" ("Department_ID") ON UPDATE CASCADE
)
WITH (
  OIDS=FALSE
);