-- Table: public.user

-- DROP TABLE IF EXISTS public."user";

CREATE TABLE IF NOT EXISTS public."user"
(
    id integer NOT NULL DEFAULT nextval('user_id_seq'::regclass),
    "user" character varying COLLATE pg_catalog."default",
    passwd character varying COLLATE pg_catalog."default",
    token character varying COLLATE pg_catalog."default",
    email character varying COLLATE pg_catalog."default",
    CONSTRAINT user_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."user"
    OWNER to postgres;


-- Table: public.convert_request

-- DROP TABLE IF EXISTS public.convert_request;

CREATE TABLE IF NOT EXISTS public.convert_request
(
    id_request integer NOT NULL DEFAULT nextval('convert_request_id_request_seq'::regclass),
    id_user integer,
    file_origin_path character varying COLLATE pg_catalog."default",
    format_request character varying COLLATE pg_catalog."default",
    status character varying COLLATE pg_catalog."default" DEFAULT 'uploaded'::character varying,
    datereg time without time zone DEFAULT now(),
    file_request_path character varying COLLATE pg_catalog."default",
    CONSTRAINT convert_request_pkey PRIMARY KEY (id_request),
    CONSTRAINT user_id_fk FOREIGN KEY (id_user)
        REFERENCES public."user" (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.convert_request
    OWNER to postgres;
    