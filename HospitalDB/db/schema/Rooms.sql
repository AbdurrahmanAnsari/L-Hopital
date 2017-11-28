-- Table: patients

-- DROP TABLE rooms;

CREATE TABLE rooms
(
    "Room_Number"  text        NOT NULL,
    "Room_Type"     text,
    CONSTRAINT room_pkey PRIMARY KEY ("Room_Number")
)
WITH (
  OIDS=FALSE
);