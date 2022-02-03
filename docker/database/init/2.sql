--
-- PostgreSQL database dump
--

-- Dumped from database version 14.1 (Debian 14.1-1.pgdg110+1)
-- Dumped by pg_dump version 14.1 (Ubuntu 14.1-1.pgdg21.04+1)

-- Started on 2022-02-03 14:37:59 MSK
--SET connection TO reference;

\c reference

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;




SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 210 (class 1259 OID 985010)
-- Name: ref_acts; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ref_acts (
    id integer NOT NULL,
    uid uuid NOT NULL,
    title character varying(255) NOT NULL,
    regex text NOT NULL,
    code integer NOT NULL
);


--
-- TOC entry 3408 (class 0 OID 0)
-- Dependencies: 210
-- Name: TABLE ref_acts; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON TABLE public.ref_acts IS 'Типы актов';


--
-- TOC entry 3409 (class 0 OID 0)
-- Dependencies: 210
-- Name: COLUMN ref_acts.id; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.ref_acts.id IS 'Первичный ключ';


--
-- TOC entry 3410 (class 0 OID 0)
-- Dependencies: 210
-- Name: COLUMN ref_acts.uid; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.ref_acts.uid IS 'Уникальный идентификатор';


--
-- TOC entry 3411 (class 0 OID 0)
-- Dependencies: 210
-- Name: COLUMN ref_acts.title; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.ref_acts.title IS 'Описание';


--
-- TOC entry 3412 (class 0 OID 0)
-- Dependencies: 210
-- Name: COLUMN ref_acts.regex; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.ref_acts.regex IS 'Описание в виде паттерна регулярного выражения';


--
-- TOC entry 3413 (class 0 OID 0)
-- Dependencies: 210
-- Name: COLUMN ref_acts.code; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.ref_acts.code IS 'Значение в виде кода (целое число)';


--
-- TOC entry 209 (class 1259 OID 985009)
-- Name: ref_acts_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.ref_acts_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3414 (class 0 OID 0)
-- Dependencies: 209
-- Name: ref_acts_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.ref_acts_id_seq OWNED BY public.ref_acts.id;


--
-- TOC entry 212 (class 1259 OID 985022)
-- Name: ref_control_level; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ref_control_level (
    id integer NOT NULL,
    uid uuid NOT NULL,
    title character varying(255) NOT NULL,
    regex text NOT NULL,
    gisok_alias text,
    code integer
);


--
-- TOC entry 3415 (class 0 OID 0)
-- Dependencies: 212
-- Name: TABLE ref_control_level; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON TABLE public.ref_control_level IS 'Уровень контроля ОТ';


--
-- TOC entry 3416 (class 0 OID 0)
-- Dependencies: 212
-- Name: COLUMN ref_control_level.id; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.ref_control_level.id IS 'Первичный ключ';


--
-- TOC entry 3417 (class 0 OID 0)
-- Dependencies: 212
-- Name: COLUMN ref_control_level.uid; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.ref_control_level.uid IS 'Уникальный идентификатор';


--
-- TOC entry 3418 (class 0 OID 0)
-- Dependencies: 212
-- Name: COLUMN ref_control_level.title; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.ref_control_level.title IS 'Описание';


--
-- TOC entry 3419 (class 0 OID 0)
-- Dependencies: 212
-- Name: COLUMN ref_control_level.regex; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.ref_control_level.regex IS 'Описание в виде паттерна регулярного выражения';


--
-- TOC entry 3420 (class 0 OID 0)
-- Dependencies: 212
-- Name: COLUMN ref_control_level.code; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.ref_control_level.code IS 'Значение в виде кода (целое число)';


--
-- TOC entry 211 (class 1259 OID 985021)
-- Name: ref_control_level_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.ref_control_level_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3421 (class 0 OID 0)
-- Dependencies: 211
-- Name: ref_control_level_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.ref_control_level_id_seq OWNED BY public.ref_control_level.id;


--
-- TOC entry 224 (class 1259 OID 985108)
-- Name: ref_control_org; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ref_control_org (
    id integer NOT NULL,
    uid uuid NOT NULL,
    regex text NOT NULL,
    title text NOT NULL,
    code integer NOT NULL
);


--
-- TOC entry 3422 (class 0 OID 0)
-- Dependencies: 224
-- Name: TABLE ref_control_org; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON TABLE public.ref_control_org IS 'Органы, проверяющие на соответствие ОТ; органы, выдающие информацию и т.д.';


--
-- TOC entry 3423 (class 0 OID 0)
-- Dependencies: 224
-- Name: COLUMN ref_control_org.id; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.ref_control_org.id IS 'Первичный ключ';


--
-- TOC entry 3424 (class 0 OID 0)
-- Dependencies: 224
-- Name: COLUMN ref_control_org.uid; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.ref_control_org.uid IS 'Уникальный идентификатор';


--
-- TOC entry 3425 (class 0 OID 0)
-- Dependencies: 224
-- Name: COLUMN ref_control_org.regex; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.ref_control_org.regex IS 'Описание в виде паттерна регулярного выражения';


--
-- TOC entry 3426 (class 0 OID 0)
-- Dependencies: 224
-- Name: COLUMN ref_control_org.title; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.ref_control_org.title IS 'Описание';


--
-- TOC entry 3427 (class 0 OID 0)
-- Dependencies: 224
-- Name: COLUMN ref_control_org.code; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.ref_control_org.code IS 'Значение в виде кода (целое число)';


--
-- TOC entry 223 (class 1259 OID 985107)
-- Name: ref_control_org_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.ref_control_org_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3428 (class 0 OID 0)
-- Dependencies: 223
-- Name: ref_control_org_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.ref_control_org_id_seq OWNED BY public.ref_control_org.id;


--
-- TOC entry 220 (class 1259 OID 985083)
-- Name: ref_publication_status; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ref_publication_status (
    id integer NOT NULL,
    uid uuid NOT NULL,
    title character varying(255) NOT NULL,
    regex text NOT NULL,
    code integer
);


--
-- TOC entry 3429 (class 0 OID 0)
-- Dependencies: 220
-- Name: TABLE ref_publication_status; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON TABLE public.ref_publication_status IS 'Статусы публикации';


--
-- TOC entry 3430 (class 0 OID 0)
-- Dependencies: 220
-- Name: COLUMN ref_publication_status.id; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.ref_publication_status.id IS 'Первичный ключ';


--
-- TOC entry 3431 (class 0 OID 0)
-- Dependencies: 220
-- Name: COLUMN ref_publication_status.uid; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.ref_publication_status.uid IS 'Уникальный идентификатор';


--
-- TOC entry 3432 (class 0 OID 0)
-- Dependencies: 220
-- Name: COLUMN ref_publication_status.title; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.ref_publication_status.title IS 'Описание';


--
-- TOC entry 3433 (class 0 OID 0)
-- Dependencies: 220
-- Name: COLUMN ref_publication_status.regex; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.ref_publication_status.regex IS 'Описание в виде паттерна регулярного выражения';


--
-- TOC entry 3434 (class 0 OID 0)
-- Dependencies: 220
-- Name: COLUMN ref_publication_status.code; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.ref_publication_status.code IS 'Значение в виде кода (целое число)';


--
-- TOC entry 219 (class 1259 OID 985082)
-- Name: ref_publication_status_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.ref_publication_status_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3435 (class 0 OID 0)
-- Dependencies: 219
-- Name: ref_publication_status_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.ref_publication_status_id_seq OWNED BY public.ref_publication_status.id;


--
-- TOC entry 222 (class 1259 OID 985096)
-- Name: ref_regulation_level; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ref_regulation_level (
    id integer NOT NULL,
    uid uuid NOT NULL,
    regex text NOT NULL,
    title character varying(255) NOT NULL,
    code integer NOT NULL
);


--
-- TOC entry 221 (class 1259 OID 985095)
-- Name: ref_regulation_level_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.ref_regulation_level_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3436 (class 0 OID 0)
-- Dependencies: 221
-- Name: ref_regulation_level_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.ref_regulation_level_id_seq OWNED BY public.ref_regulation_level.id;


--
-- TOC entry 214 (class 1259 OID 985046)
-- Name: ref_subjects; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ref_subjects (
    id integer NOT NULL,
    uid uuid NOT NULL,
    title character varying(255) NOT NULL,
    regex text NOT NULL,
    code integer NOT NULL
);


--
-- TOC entry 3437 (class 0 OID 0)
-- Dependencies: 214
-- Name: TABLE ref_subjects; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON TABLE public.ref_subjects IS 'Типы субъектов';


--
-- TOC entry 3438 (class 0 OID 0)
-- Dependencies: 214
-- Name: COLUMN ref_subjects.id; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.ref_subjects.id IS 'Первичный ключ';


--
-- TOC entry 3439 (class 0 OID 0)
-- Dependencies: 214
-- Name: COLUMN ref_subjects.uid; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.ref_subjects.uid IS 'Уникальный идентификатор';


--
-- TOC entry 3440 (class 0 OID 0)
-- Dependencies: 214
-- Name: COLUMN ref_subjects.title; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.ref_subjects.title IS 'Описание';


--
-- TOC entry 3441 (class 0 OID 0)
-- Dependencies: 214
-- Name: COLUMN ref_subjects.regex; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.ref_subjects.regex IS 'Описание в виде паттерна регулярного выражения';


--
-- TOC entry 3442 (class 0 OID 0)
-- Dependencies: 214
-- Name: COLUMN ref_subjects.code; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.ref_subjects.code IS 'Значение в виде кода (целое число)';


--
-- TOC entry 213 (class 1259 OID 985045)
-- Name: ref_subjects_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.ref_subjects_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3443 (class 0 OID 0)
-- Dependencies: 213
-- Name: ref_subjects_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.ref_subjects_id_seq OWNED BY public.ref_subjects.id;


--
-- TOC entry 216 (class 1259 OID 985058)
-- Name: ref_validity_status; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ref_validity_status (
    id integer NOT NULL,
    uid uuid NOT NULL,
    title character varying(255) NOT NULL,
    regex text NOT NULL,
    code integer
);


--
-- TOC entry 3444 (class 0 OID 0)
-- Dependencies: 216
-- Name: TABLE ref_validity_status; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON TABLE public.ref_validity_status IS 'Статусы действия ОТ';


--
-- TOC entry 3445 (class 0 OID 0)
-- Dependencies: 216
-- Name: COLUMN ref_validity_status.id; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.ref_validity_status.id IS 'Первичный ключ';


--
-- TOC entry 3446 (class 0 OID 0)
-- Dependencies: 216
-- Name: COLUMN ref_validity_status.uid; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.ref_validity_status.uid IS 'Уникальный идентификатор';


--
-- TOC entry 3447 (class 0 OID 0)
-- Dependencies: 216
-- Name: COLUMN ref_validity_status.title; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.ref_validity_status.title IS 'Описание';


--
-- TOC entry 3448 (class 0 OID 0)
-- Dependencies: 216
-- Name: COLUMN ref_validity_status.regex; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.ref_validity_status.regex IS 'Описание в виде паттерна регулярного выражения';


--
-- TOC entry 3449 (class 0 OID 0)
-- Dependencies: 216
-- Name: COLUMN ref_validity_status.code; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.ref_validity_status.code IS 'Значение в виде кода (целое число)';


--
-- TOC entry 215 (class 1259 OID 985057)
-- Name: ref_validity_status_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.ref_validity_status_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3450 (class 0 OID 0)
-- Dependencies: 215
-- Name: ref_validity_status_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.ref_validity_status_id_seq OWNED BY public.ref_validity_status.id;


--
-- TOC entry 218 (class 1259 OID 985070)
-- Name: ref_work_status; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ref_work_status (
    id integer NOT NULL,
    uid uuid NOT NULL,
    title character varying(255) NOT NULL,
    regex text NOT NULL,
    code integer
);


--
-- TOC entry 3451 (class 0 OID 0)
-- Dependencies: 218
-- Name: TABLE ref_work_status; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON TABLE public.ref_work_status IS 'Статусы работы с ОТ';


--
-- TOC entry 3452 (class 0 OID 0)
-- Dependencies: 218
-- Name: COLUMN ref_work_status.id; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.ref_work_status.id IS 'Первичный ключ';


--
-- TOC entry 3453 (class 0 OID 0)
-- Dependencies: 218
-- Name: COLUMN ref_work_status.uid; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.ref_work_status.uid IS 'Уникальный идентификатор';


--
-- TOC entry 3454 (class 0 OID 0)
-- Dependencies: 218
-- Name: COLUMN ref_work_status.title; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.ref_work_status.title IS 'Описание';


--
-- TOC entry 3455 (class 0 OID 0)
-- Dependencies: 218
-- Name: COLUMN ref_work_status.regex; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.ref_work_status.regex IS 'Описание в виде паттерна регулярного выражения';


--
-- TOC entry 3456 (class 0 OID 0)
-- Dependencies: 218
-- Name: COLUMN ref_work_status.code; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.ref_work_status.code IS 'Значение в виде кода (целое число)';


--
-- TOC entry 217 (class 1259 OID 985069)
-- Name: ref_work_status_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.ref_work_status_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3457 (class 0 OID 0)
-- Dependencies: 217
-- Name: ref_work_status_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.ref_work_status_id_seq OWNED BY public.ref_work_status.id;


--
-- TOC entry 3202 (class 2604 OID 985013)
-- Name: ref_acts id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ref_acts ALTER COLUMN id SET DEFAULT nextval('public.ref_acts_id_seq'::regclass);


--
-- TOC entry 3203 (class 2604 OID 985025)
-- Name: ref_control_level id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ref_control_level ALTER COLUMN id SET DEFAULT nextval('public.ref_control_level_id_seq'::regclass);


--
-- TOC entry 3209 (class 2604 OID 985111)
-- Name: ref_control_org id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ref_control_org ALTER COLUMN id SET DEFAULT nextval('public.ref_control_org_id_seq'::regclass);


--
-- TOC entry 3207 (class 2604 OID 985086)
-- Name: ref_publication_status id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ref_publication_status ALTER COLUMN id SET DEFAULT nextval('public.ref_publication_status_id_seq'::regclass);


--
-- TOC entry 3208 (class 2604 OID 985099)
-- Name: ref_regulation_level id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ref_regulation_level ALTER COLUMN id SET DEFAULT nextval('public.ref_regulation_level_id_seq'::regclass);


--
-- TOC entry 3204 (class 2604 OID 985049)
-- Name: ref_subjects id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ref_subjects ALTER COLUMN id SET DEFAULT nextval('public.ref_subjects_id_seq'::regclass);


--
-- TOC entry 3205 (class 2604 OID 985061)
-- Name: ref_validity_status id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ref_validity_status ALTER COLUMN id SET DEFAULT nextval('public.ref_validity_status_id_seq'::regclass);


--
-- TOC entry 3206 (class 2604 OID 985073)
-- Name: ref_work_status id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ref_work_status ALTER COLUMN id SET DEFAULT nextval('public.ref_work_status_id_seq'::regclass);


-- --
-- TOC entry 3387 (class 0 OID 985010)
-- Dependencies: 210
-- Data for Name: ref_acts; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.ref_acts VALUES (2, '4a41ded7-630b-4eae-a4e6-957a9db4a350', 'Постановление федерального органа исполнительной власти', '^постан[а-я]+.*федер[а-я].*орг[а-я]+.*испол[а-я]+.*$', 0);
INSERT INTO public.ref_acts VALUES (3, 'f156ebd8-afe9-4e41-a0d3-1f9935d09ce1', 'Федеральный закон', '^федер[а-я]+.*зак[а-я]+$', 1);
INSERT INTO public.ref_acts VALUES (4, '19a5ed94-6beb-4b10-87b0-8891360bab65', 'Приказ федерального органа исполнительной власти', '^прик[а-я]+.*федер[а-я]+.*орг[а-я]+.*исполн[а-я]+.*$', 2);
INSERT INTO public.ref_acts VALUES (5, '0ad62f1e-7f08-4fda-9571-829166da826b', 'Постановление Правительства Российской Федерации', '^постан[а-я]+.*правит[а-я]+.*рос[а-я]+.*фед[а-я].*$', 3);
INSERT INTO public.ref_acts VALUES (6, '30fdb8de-9aec-4eaf-9cb1-2bcfc00f389a', 'Акт СССР', '^акт.*ссср.*$', 4);
INSERT INTO public.ref_acts VALUES (7, '06c660a1-b33c-40a8-a080-7f8db71135e1', 'Правила федерального органа исполнительной власти', '^прав[а-я]+.*фед[а-я]+.*орг[а-я]+.*исполн[а-я]+.*власт[а-я]+.*$', 5);
INSERT INTO public.ref_acts VALUES (8, 'f792e6dc-bb11-4091-83af-7ccc973a4838', 'Положение федерального органа  исполнительной власти', '^полож[а-я]+.*фед[а-я]+.*орг[а-я]+.*исполнит[а-я]+.*власт[а-я]+.*$', 8);
INSERT INTO public.ref_acts VALUES (9, '11a2e0a2-0d63-4eb6-b5ba-3747606c7f2e', 'Решение Коллегии Евразийской Экономической Комиссии', '^реш[а-я]+.*колл[а-я]+.*евраз[а-я]+.*эконом[а-я]+.*комисс[а-я]+.*$', 9);
INSERT INTO public.ref_acts VALUES (10, 'bc541d3a-e9d3-49e6-adb8-8b15602f349c', 'Решение Комиссии Таможенного союза', '^реш[а-я]+.*комм[а-я]+.*тамож[а-я]+.*союз[а-я]+.*$', 10);
INSERT INTO public.ref_acts VALUES (11, '72eef61f-0de0-4ac8-bd8e-477c170647fb', 'Решение Совета Евразийской экономической комиссии', '^реш[а-я]+.*совет[а-я]+.*евраз[а-я]+.*экономич[а-я]+.*комисс[а-я]+.*$', 11);
INSERT INTO public.ref_acts VALUES (12, '0961a24b-8e50-4081-84c2-0f9ffc4cc9f6', 'Федеральный конституционный закон', '^фед[а-я]+.*конст[а-я]+.*зак[а-я]+.*', 12);


--
-- TOC entry 3389 (class 0 OID 985022)
-- Dependencies: 212
-- Data for Name: ref_control_level; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.ref_control_level VALUES (1, '42238629-d7ec-470c-97cb-edccd64bd08d', 'Федеральный государственный надзор за соблюдением трудового законодательства и иных нормативных правовых актов, содержащих нормы трудового права', '(федер[а-я]+).+(госуд[а-я]+).*(труд[а-я]+).+(закон[а-я]+).+(труд[а-я]+).+(прав[а-я]+).*', 'Федеральный государственный надзор за соблюдением трудового законодательства и иных нормативных правовых актов, содержащих нормы трудового права', 0);
INSERT INTO public.ref_control_level VALUES (2, '7b8960fb-45b0-49e3-aa48-1f038c1e72b6', 'Федеральный государственный контроль (надзор) за деятельностью аккредитованных лиц', '(федер[а-я]+).+(госуд[а-я]+).+(деят[а-я]+).+(аккред[а-я]+).+(лиц[а-я]*).*', 'Федеральный государственный контроль за деятельностью аккредитованных лиц', 1);
INSERT INTO public.ref_control_level VALUES (15, 'b118e66c-533f-4cfa-88d7-58d39ad46a39', 'Федеральный государственный санитарно-эпидемиологический контроль (надзор)', '(федерал[а-я]+).*(государ[а-я]+).*(санитар[а-я]+).*(эпидем[а-я]*).*(конт[а-я]*).*', 'Федеральный государственный санитарно-эпидемиологический надзор', 14);
INSERT INTO public.ref_control_level VALUES (16, '82aaf0f7-2c4a-45af-9f0e-744774843a2e', 'Государственный контроль (надзор) за деятельностью саморегулируемых организаций аудиторов', '(государ[а-я]+).*(контро[а-я]+).*(деятел[а-я]+).*(саморегул[а-я]*).*(орган[а-я]*).*(аудит[а-я]*).*', 'Государственный контроль (надзор) за деятельностью саморегулируемых организаций аудиторов', 15);
INSERT INTO public.ref_control_level VALUES (17, '154692af-35bb-41fc-be80-b85b6ba7add8', 'Федеральный государственный контроль (надзор) в области защиты прав потребителей', '(федерал[а-я]+).*(государств[а-я]+).*(контрол[а-я]+).*(област[а-я]*).*(защит[а-я]*).*(прав[а-я]*).*(потребит[а-я]*).*', 'Федеральный государственный надзор в области защиты прав потребителей', 16);
INSERT INTO public.ref_control_level VALUES (10, '1a1939fc-9ce5-4c5f-a320-43ad9eac2d44', 'Федеральный государственный лицензионный контроль (надзор) за деятельностью по тушению пожаров в населенных пунктах, на производственных объектах и объектах инфраструктуры', '(федерал[а-я]+).*(государ[а-я]+).*(лиценз[а-я]+).+(деятел[а-я]+).+(тушен[а-я]+).+(пожар[а-я]+).+(населен[а-я]*).*(пункт[а-я]*).*(производ[а-я]*).*(объект[а-я]*).*(объект[а-я]*).*(инфраструк[а-я]*).*', 'Отсутствует', 9);
INSERT INTO public.ref_control_level VALUES (3, 'd9a8a3dc-77b0-441c-bd3a-511e221ab30d', 'Аккредитация юридических лиц и индивидуальных предпринимателей в национальной системе аккредитации', '(аккред[а-я]+).+(юридич[а-я]+).+(индивид[а-я]+).+(предприн[а-я]+).+(нац[а-я]*).*(сист[а-я]*).*(аккре[а-я]*).*', 'Отсутствует', 2);
INSERT INTO public.ref_control_level VALUES (4, 'e67af27f-da5b-4c7a-8d2f-2c37d4c62199', 'Федеральный государственный контроль (надзор) на автомобильном транспорте, городском наземном электрическом транспорте и в дорожном хозяйстве', '(федер[а-я]+).+(госуд[а-я]+).+(контро[а-я]+).+(автомоб[а-я]+).+(транспор[а-я]*).*(городск[а-я]*).*(наземн[а-я]*).*.*(электрич[а-я]*).*(дорож[а-я]*).*(хозяйств[а-я]*)', 'Отсутствует', 3);
INSERT INTO public.ref_control_level VALUES (5, '736de6d5-b3d6-44b6-8044-a4e85ee817a0', 'Лицензирование деятельности по перевозкам пассажиров и иных лиц автобусами', '(лиценз[а-я]+).+(деят[а-я]+).+(перевозк[а-я]+).+(пассаж[а-я]+).+(иных[а-я]*).*(лиц[а-я]*).*(автобус[а-я]*).*.', 'Отсутствует', 4);
INSERT INTO public.ref_control_level VALUES (6, 'c924c7bb-2695-431f-a83a-ef15e82b60fc', 'Лицензионный контроль в отношении лиц, осуществляющих управление многоквартирными домами', '(лиценз[а-я]+).+(конт[а-я]+).+(осуществл[а-я]+).+(управ[а-я]+).+(многоквартир[а-я]*).*(дом[а-я]*).*', 'Лицензионный контроль в отношении лиц, осуществляющих управление многоквартирными домами', 5);
INSERT INTO public.ref_control_level VALUES (7, 'd6ce6b53-82ae-43dc-ab79-1529ab93415a', 'Лицензирование образовательной деятельности (за исключением указанной деятельности, осуществляемой частными образовательными организациями на территории инновационного центра "Сколково")', '(лиценз[а-я]+).+(образов[а-я]+).+(деятел[а-я]+).+(инновац[а-я]+).+(центр[а-я]*).*(сколково[а-я]*).*', 'Отсутствует', 6);
INSERT INTO public.ref_control_level VALUES (8, '543eff31-a414-4eba-9022-76ec2ed4ada3', 'Лицензирование деятельности по монтажу, техническому обслуживанию и ремонту средств обеспечения пожарной безопасности зданий и сооружений', '(лиценз[а-я]+).+(деятел[а-я]+).+(монтаж[а-я]+).+(обслужива[а-я]+).+(ремонт[а-я]*).*(средств[а-я]*).*(обеспеч[а-я]*).*(пожар[а-я]*).*(безопаснос[а-я]*).*(здани[а-я]*).*(сооружени[а-я]*).*', 'Отсутствует', 7);
INSERT INTO public.ref_control_level VALUES (9, '8bf16b3e-04cc-46e5-bc8d-38782177404e', 'Лицензирование деятельности по тушению пожаров в населенных пунктах, на производственных объектах и объектах инфраструктуры', '(лиценз[а-я]+).+(деятел[а-я]+).+(тушен[а-я]+).+(пожар[а-я]+).+(населен[а-я]*).*(пункт[а-я]*).*(производ[а-я]*).*(объект[а-я]*).*(объект[а-я]*).*(инфраструк[а-я]*).*', 'Отсутствует', 8);
INSERT INTO public.ref_control_level VALUES (12, 'fc0fd652-1078-42d5-bda8-3079145a7ddf', 'Федеральный государственный контроль (надзор) в сфере образования', '(федерал[а-я]+).*(государ[а-я]+).*(контрол[а-я]+).+(сфер[а-я]+).+(образова[а-я]+).*', 'Федеральный государственный контроль (надзор) в сфере образования', 11);
INSERT INTO public.ref_control_level VALUES (13, 'dd9e285c-8f88-4e3f-919d-090d77186c64', 'Федеральный государственный лицензионный контроль (надзор) за деятельностью по монтажу, техническому обслуживанию и ремонту средств обеспечения пожарной безопасности зданий и сооружений', '(федерал[а-я]+).*(государ[а-я]+).*(лиценз[а-я]+).+(контрол[а-я]+).+(деяте[а-я]+).+(монтаж[а-я]+).*(обслужив[а-я]+).*(ремонт[а-я]+).*(средств[а-я]*).*(обеспечени[а-я]+).*(пожар[а-я]+).*(безопасн[а-я]+).*(здан[а-я]+).*(сооруж[а-я]+).*', 'Отсутствует', 12);
INSERT INTO public.ref_control_level VALUES (14, '7a6e678a-9bb9-4981-bb9c-d572d82fdae5', 'Федеральный государственный пожарный надзор', '(федерал[а-я]+).*(государ[а-я]+).*(пожарн[а-я]+).*(надзор[а-я]*).*', 'Федеральный государственный пожарный надзор', 13);
INSERT INTO public.ref_control_level VALUES (11, '2e575622-c51b-4d30-b7fb-8f3354492353', 'Федеральный государственный контроль (надзор) за деятельностью юридических лиц, осуществляющих деятельность по возврату просроченной задолженности в качестве основного вида деятельности, включенных в государственный реестр', '(федерал[а-я]+).*(государ[а-я]+).*(контрол[а-я]+).+(деятел[а-я]+).+(юридич[а-я]+).+(лиц[а-я]*).+(осуществл[а-я]+).*(деятел[а-я]*).*(возврат[а-я]*).*(просроч[а-я]*).*(задолжен[а-я]*).*(включен[а-я]*).*(государ[а-я]*).*(реестр[а-я]*).*', 'Федеральный государственный контроль (надзор) за деятельностью юридических лиц, осуществляющих деятельность по возврату просроченной задолженности в качестве основного вида деятельности, включенных в государственный реестр', 10);


--
-- TOC entry 3401 (class 0 OID 985108)
-- Dependencies: 224
-- Data for Name: ref_control_org; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.ref_control_org VALUES (22, '0d1508a5-691e-4667-8759-4a0fc57e9dc8', '^мин[а-я]+.*обор[а-я]+.*$', 'Министерство обороны Российской Федерации', 21);
INSERT INTO public.ref_control_org VALUES (1, 'eaacaea4-ef10-4189-81c3-894fbef7ec0a', '^фед[а-я]+.*служ[а-я]+.*труд[а-я]+.*занят[а-я]+.*$', 'Федеральная служба по труду и занятости', 0);
INSERT INTO public.ref_control_org VALUES (2, '6a290668-9c72-4dc5-876c-4ee6c4d4c335', '^фед[а-я]+.*служ[а-я]+.*аккред[а-я]+.*$', 'Федеральная служба по аккредитации', 1);
INSERT INTO public.ref_control_org VALUES (3, '3f4a2091-41e9-484c-b4ed-3e9a5a1ddf71', '^фед[а-я]+.*служ[а-я]+.*надзор[а-я]+.*сфер[а-я]+.*трансп[а-я]+.*$', 'Федеральная служба по надзору в сфере транспорта', 2);
INSERT INTO public.ref_control_org VALUES (4, '83bfb5e8-d0c4-4047-a162-c5d9fdd7ccdf', '^мин[а-я]+.*стро[а-я]+.*жил[а-я]+.*комм[а-я]+.*хоз[а-я]+.*$', 'Министерство строительства и жилищно-коммунального хозяйства Российской Федерации', 3);
INSERT INTO public.ref_control_org VALUES (5, '5dbac1f5-c273-4753-a92a-26d9c58a59e5', '^фед[а-я]+.*служ[а-я]+.*надзор[а-я]+.*сфер[а-я]+.*защ[а-я]+.*прав[а-я]*.*потреб[а-я]+.*благополуч[а-я]+.*чел[а-я]+.*$', 'Федеральная служба по надзору в сфере защиты прав потребителей и благополучия человека', 4);
INSERT INTO public.ref_control_org VALUES (6, '07655548-e2dc-48fe-8099-fd413b3d6789', '^мин[а-я]+.*юстиц[а-я]+.*$', 'Министерство юстиции Российской Федерации', 5);
INSERT INTO public.ref_control_org VALUES (7, 'd3dfe524-221c-4f95-98ab-91986eb3d194', '^фед[а-я]+.*служб[а-я]+.*надзор[а-я]+.*сфер[а-я]+.*образов[а-я]+.*наук[а-я]+.*$', 'Федеральная служба по надзору в сфере образования и науки', 6);
INSERT INTO public.ref_control_org VALUES (8, '354777d2-bbf0-497a-a020-a0fa744ab07d', '^мин[а-я]+.*дел[а-я]+.*гражд[а-я]+.*обор[а-я]+.*чрезв[а-я]+.*ситуац[а-я]+.*ликвидац[а-я]+.*послед[а-я]+.*стих[а-я]+.*бед[а-я]+.*$', 'Министерство Российской Федерации по делам гражданской обороны, чрезвычайным ситуациям и ликвидации последствий стихийных бедствий', 7);
INSERT INTO public.ref_control_org VALUES (9, '97e65797-6c86-45f8-9320-1226b772eac9', '^главн[а-я]+.*управ[а-я]+.*спец[а-я].*прог[а-я]+.*$', 'Главное управление специальных программ Президента Российской Федерации', 8);
INSERT INTO public.ref_control_org VALUES (10, '98de3934-73e1-43b1-b69b-4b9bd310cf40', '^фед[а-я]+.*аген[а-я]+.*технич[а-я].*регул[а-я]+.*метрол[а-я]+.*$', 'Федеральное агентство по техническому регулированию и метрологии', 9);
INSERT INTO public.ref_control_org VALUES (11, 'f5896e5d-2838-4cb5-9221-a199accc7b54', '^фед[а-я]+.*служ[а-я]+.*экологич[а-я].*технолог[а-я]+.*атом[а-я]+.*надзор[а-я]+.*$', 'Федеральная служба по экологическому, технологическому и атомному надзору', 10);
INSERT INTO public.ref_control_org VALUES (12, 'c79d567e-1e5f-4b42-9e07-81a229137361', '^мин[а-я]+.*внутр[а-я]+.*дел[а-я].*$', 'Министерство внутренних дел Российской Федерации', 11);
INSERT INTO public.ref_control_org VALUES (13, 'cbce62ff-5261-43d9-9e0a-aa54abd0ad1b', '^фед[а-я]+.*аген[а-я]+.*мор[а-я].*реч[а-я]+.*трансп[а-я]+.*$', 'Федеральное агентство морского и речного транспорта', 12);
INSERT INTO public.ref_control_org VALUES (14, '9e8f5709-b948-40d3-8ef9-ccc09ef4bd79', '^фед[а-я]+.*служб[а-я]+.*надзор[а-я].*сфер[а-я]+.*связ[а-я]+.*информац[а-я]+.*техн[а-я]+.*масс[а-я]+.*комм[а-я]+.*$', 'Федеральная служба по надзору в сфере связи, информационных технологий и массовых коммуникаций', 13);
INSERT INTO public.ref_control_org VALUES (15, '8194ac91-8cf6-42fb-8ccb-c400d55ccf63', '^фед[а-я]+.*служб[а-я]+.*ветер[а-я].*фито[а-я]+.*надзор[а-я]+.*$', 'Федеральная служба по ветеринарному и фитосанитарному надзору', 14);
INSERT INTO public.ref_control_org VALUES (16, 'b5464ca2-8636-4cef-ae7e-dbd856e6366a', '^мин[а-я]+.*сел[а-я]+.*хоз[а-я].*$', 'Министерство сельского хозяйства Российской Федерации', 15);
INSERT INTO public.ref_control_org VALUES (17, 'de192caa-109d-4096-92b6-bbcec5db748d', '^фед[а-я]+.*аген[а-я]+.*возд[а-я].*тран[а-я]+.*$', 'Федеральное агентство воздушного транспорта', 16);
INSERT INTO public.ref_control_org VALUES (20, '86253a4b-33ed-4219-969c-80f896babb71', '^фед[а-я]+.*служ[а-я]+.*гос[а-я]+.*рег[а-я]+.*кадас[а-я]+.*картограф[а-я]+.*$', 'Федеральная служба государственной регистрации, кадастра и картографии', 18);
INSERT INTO public.ref_control_org VALUES (19, 'f7a29299-e0db-4e2e-a1da-95464ac9856d', '^фед[а-я]+.*мед[а-я]+.*биол[а-я]+.*аген[а-я]+.*$', 'Федеральное медико-биологическое агентство', 19);
INSERT INTO public.ref_control_org VALUES (21, '2bc4c800-65da-4efa-9398-341cefc5646e', '^орг[а-я]+.*гос[а-я]+.*власт[а-я]+.*суб[а-я]+.*перед[а-я]+.*полномоч[а-я]+.*контрол[а-я]+.*надзор[а-я]+.*$', 'Органы государственной власти субъектов Российской Федерации, которым переданы полномочия по контролю (надзору)', 20);
INSERT INTO public.ref_control_org VALUES (23, '6ebb5cb2-2dba-4ad7-baad-d9bd0dcefedc', '^фед[а-я]+.*служ[а-я]+.*безоп[а-я].*$', 'Федеральная служба безопасности Российской Федерации', 22);
INSERT INTO public.ref_control_org VALUES (24, 'b6069a00-1915-4b70-aed1-7fea2a88ccb6', '^фед[а-я]+.*служ[а-я]+.*войск[а-я]*.*нац[а-я]+.*гвард[а-я]+.*$', 'Федеральная служба войск национальной гвардии Российской Федерации', 23);
INSERT INTO public.ref_control_org VALUES (25, '6f729ec1-5518-44f7-86b2-1cb39f3a6dc9', '^фед[а-я]+.*служ[а-я]+.*охран[а-я]*.*$', 'Федеральная служба охраны Российской Федерации', 24);
INSERT INTO public.ref_control_org VALUES (18, '616385cb-13dc-4239-a85d-11d60abcb8c9', '^фед[а-я]+.*каз[а-я]+.*учр[а-я].*форм[а-я]+.*гос[а-я]+.*фонд[а-я]+.*драг[а-я]+.*мет[а-я]+.*драг[а-я]+.*камн[а-я]+.*гохран.*$', 'Федеральное казенное учреждение «Государственное учреждение по формированию государственного фонда драгоценных металлов и драгоценных камней Российской Федерации, хранению, отпуску и использованию драгоценных металлов и драгоценных камней (Гохран России) при Министерстве финансов Российской Федерации»', 17);


--
-- TOC entry 3397 (class 0 OID 985083)
-- Dependencies: 220
-- Data for Name: ref_publication_status; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.ref_publication_status VALUES (1, 'fe432c97-77ff-451a-aa09-b05c8ea18dc3', 'снято с публикации', 'снят[а-я]+', 0);
INSERT INTO public.ref_publication_status VALUES (3, '2cf026aa-2cff-461f-b1a1-ac15a6c588d8', 'есть неопубликованные изменения', 'неопубликованн[а-я]+\s*изменен[а-я]+', 2);
INSERT INTO public.ref_publication_status VALUES (4, 'fe8b4994-7083-4e48-9b45-213b42946a3a', 'ошибка при публикации', 'ошиб[а-я]+', 3);
INSERT INTO public.ref_publication_status VALUES (5, 'ae9d2eca-ae63-4442-9dfa-ac85cbf2f26e', 'не было опубликовано', 'не.+(был[а-я]+.+)?опубликов[а-я]+.*', 5);
INSERT INTO public.ref_publication_status VALUES (2, 'aecb0304-9c59-4f75-92ac-712cb007457a', 'успешно', '.*успешн[а-я]+.*', 1);


--
-- TOC entry 3399 (class 0 OID 985096)
-- Dependencies: 222
-- Data for Name: ref_regulation_level; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.ref_regulation_level VALUES (1, 'e941e795-1a5a-48a1-9333-b3fad66740e2', '^.*федерал[а-я]+.*$', 'Федеральный уровень', 1);
INSERT INTO public.ref_regulation_level VALUES (2, 'da73687c-4150-4345-9745-2499c24f8fa6', '^.*регион[а-я]+.*$', 'Региональный уровень', 0);


--
-- TOC entry 3391 (class 0 OID 985046)
-- Dependencies: 214
-- Data for Name: ref_subjects; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.ref_subjects VALUES (1, 'e4b2c6ae-5e53-4b2c-9e83-73609dece588', 'Физические лица, зарегистрированные как ИП', '^физ[a-я]+.*лиц[а-я]*.*[ип]$', 0);
INSERT INTO public.ref_subjects VALUES (2, 'edda853d-883e-401c-b0d2-ee4b207380bc', 'Физические лица', '^физ[a-я]+.*лиц[а-я]*.*$', 1);
INSERT INTO public.ref_subjects VALUES (3, '0aa34501-a237-4b68-823e-2766f26644c5', 'Юридические лица', '^юр[a-я]+.*лиц[а-я]*.*$', 2);
INSERT INTO public.ref_subjects VALUES (4, '4dfe4314-fd4c-41ce-b0dc-c683a8b42def', 'Должностные лица', '^должн[a-я]+.*лиц[а-я]*.*$', 3);


--
-- TOC entry 3393 (class 0 OID 985058)
-- Dependencies: 216
-- Data for Name: ref_validity_status; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.ref_validity_status VALUES (1, '5bdafe10-9d10-4f2a-bc9a-b3d341088e8f', 'Действующее', '^действ[a-я]+$', 1);
INSERT INTO public.ref_validity_status VALUES (2, '853b1655-aa8c-4781-bad5-a163783f4f60', 'Недействующее', '^недейств[a-я]+$', 0);


--
-- TOC entry 3395 (class 0 OID 985070)
-- Dependencies: 218
-- Data for Name: ref_work_status; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.ref_work_status VALUES (1, '9bacdcf5-b249-4350-9395-40d493f67009', 'Проверка атрибутов ОТ', '^провер[а-я]+.*атриб[а-я]+.*(от|обязат[а-я]+.*треб[а-я]+).*$', NULL);
INSERT INTO public.ref_work_status VALUES (2, '2234d98d-89d5-4dc7-995d-7566ee0b3c3b', 'Утверждено', '^утвер[а-я]+.*$', NULL);


--
-- TOC entry 3458 (class 0 OID 0)
-- Dependencies: 209
-- Name: ref_acts_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.ref_acts_id_seq', 12, true);


--
-- TOC entry 3459 (class 0 OID 0)
-- Dependencies: 211
-- Name: ref_control_level_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.ref_control_level_id_seq', 17, true);


--
-- TOC entry 3460 (class 0 OID 0)
-- Dependencies: 223
-- Name: ref_control_org_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.ref_control_org_id_seq', 25, true);


--
-- TOC entry 3461 (class 0 OID 0)
-- Dependencies: 219
-- Name: ref_publication_status_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.ref_publication_status_id_seq', 6, true);


--
-- TOC entry 3462 (class 0 OID 0)
-- Dependencies: 221
-- Name: ref_regulation_level_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.ref_regulation_level_id_seq', 2, true);


--
-- TOC entry 3463 (class 0 OID 0)
-- Dependencies: 213
-- Name: ref_subjects_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.ref_subjects_id_seq', 4, true);


--
-- TOC entry 3464 (class 0 OID 0)
-- Dependencies: 215
-- Name: ref_validity_status_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.ref_validity_status_id_seq', 2, true);


--
-- TOC entry 3465 (class 0 OID 0)
-- Dependencies: 217
-- Name: ref_work_status_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.ref_work_status_id_seq', 2, true);


--
-- TOC entry 3212 (class 2606 OID 985017)
-- Name: ref_acts ref_acts_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ref_acts
    ADD CONSTRAINT ref_acts_pkey PRIMARY KEY (id);


--
-- TOC entry 3214 (class 2606 OID 985019)
-- Name: ref_acts ref_acts_title_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ref_acts
    ADD CONSTRAINT ref_acts_title_key UNIQUE (title);


--
-- TOC entry 3217 (class 2606 OID 985029)
-- Name: ref_control_level ref_control_level_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ref_control_level
    ADD CONSTRAINT ref_control_level_pkey PRIMARY KEY (id);


--
-- TOC entry 3219 (class 2606 OID 985031)
-- Name: ref_control_level ref_control_level_title_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ref_control_level
    ADD CONSTRAINT ref_control_level_title_key UNIQUE (title);


--
-- TOC entry 3246 (class 2606 OID 985115)
-- Name: ref_control_org ref_control_org_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ref_control_org
    ADD CONSTRAINT ref_control_org_pkey PRIMARY KEY (id);


--
-- TOC entry 3237 (class 2606 OID 985090)
-- Name: ref_publication_status ref_publication_status_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ref_publication_status
    ADD CONSTRAINT ref_publication_status_pkey PRIMARY KEY (id);


--
-- TOC entry 3239 (class 2606 OID 985092)
-- Name: ref_publication_status ref_publication_status_title_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ref_publication_status
    ADD CONSTRAINT ref_publication_status_title_key UNIQUE (title);


--
-- TOC entry 3242 (class 2606 OID 985103)
-- Name: ref_regulation_level ref_regulation_level_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ref_regulation_level
    ADD CONSTRAINT ref_regulation_level_pkey PRIMARY KEY (id);


--
-- TOC entry 3244 (class 2606 OID 985105)
-- Name: ref_regulation_level ref_regulation_level_title_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ref_regulation_level
    ADD CONSTRAINT ref_regulation_level_title_key UNIQUE (title);


--
-- TOC entry 3222 (class 2606 OID 985053)
-- Name: ref_subjects ref_subjects_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ref_subjects
    ADD CONSTRAINT ref_subjects_pkey PRIMARY KEY (id);


--
-- TOC entry 3224 (class 2606 OID 985055)
-- Name: ref_subjects ref_subjects_title_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ref_subjects
    ADD CONSTRAINT ref_subjects_title_key UNIQUE (title);


--
-- TOC entry 3227 (class 2606 OID 985065)
-- Name: ref_validity_status ref_validity_status_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ref_validity_status
    ADD CONSTRAINT ref_validity_status_pkey PRIMARY KEY (id);


--
-- TOC entry 3229 (class 2606 OID 985067)
-- Name: ref_validity_status ref_validity_status_title_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ref_validity_status
    ADD CONSTRAINT ref_validity_status_title_key UNIQUE (title);


--
-- TOC entry 3232 (class 2606 OID 985077)
-- Name: ref_work_status ref_work_status_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ref_work_status
    ADD CONSTRAINT ref_work_status_pkey PRIMARY KEY (id);


--
-- TOC entry 3234 (class 2606 OID 985079)
-- Name: ref_work_status ref_work_status_title_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ref_work_status
    ADD CONSTRAINT ref_work_status_title_key UNIQUE (title);


--
-- TOC entry 3210 (class 1259 OID 985020)
-- Name: idx_ref_acts_title_1e9a3d; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX idx_ref_acts_title_1e9a3d ON public.ref_acts USING btree (title);


--
-- TOC entry 3215 (class 1259 OID 985032)
-- Name: idx_ref_control_title_c38947; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX idx_ref_control_title_c38947 ON public.ref_control_level USING btree (title);


--
-- TOC entry 3235 (class 1259 OID 985093)
-- Name: idx_ref_publica_title_07fe19; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX idx_ref_publica_title_07fe19 ON public.ref_publication_status USING btree (title);


--
-- TOC entry 3240 (class 1259 OID 985106)
-- Name: idx_ref_regulat_title_367d46; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX idx_ref_regulat_title_367d46 ON public.ref_regulation_level USING btree (title);


--
-- TOC entry 3220 (class 1259 OID 985056)
-- Name: idx_ref_subject_title_54d1a2; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX idx_ref_subject_title_54d1a2 ON public.ref_subjects USING btree (title);


--
-- TOC entry 3225 (class 1259 OID 985068)
-- Name: idx_ref_validit_title_c3a4db; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX idx_ref_validit_title_c3a4db ON public.ref_validity_status USING btree (title);


--
-- TOC entry 3230 (class 1259 OID 985080)
-- Name: idx_ref_work_st_title_ebf137; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX idx_ref_work_st_title_ebf137 ON public.ref_work_status USING btree (title);


-- Completed on 2022-02-03 14:38:00 MSK

--
-- PostgreSQL database dump complete
--

