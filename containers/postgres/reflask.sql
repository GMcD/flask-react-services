--
-- PostgreSQL database dump
--

-- Dumped from database version 12.4
-- Dumped by pg_dump version 12.4

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
-- Name: reflask_posts; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.reflask_posts (
    id integer NOT NULL,
    title character varying(128) NOT NULL,
    content text
);


--
-- Name: reflask_posts_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.reflask_posts_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: reflask_posts_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.reflask_posts_id_seq OWNED BY public.reflask_posts.id;


--
-- Name: reflask_users; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.reflask_users (
    id integer NOT NULL,
    google character varying(64),
    username character varying(64) NOT NULL,
    email character varying(256) NOT NULL,
    created timestamp without time zone NOT NULL,
    bio text,
    avatar text,
    admin boolean NOT NULL,
    password_hash character varying(128)
);


--
-- Name: reflask_users_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.reflask_users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: reflask_users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.reflask_users_id_seq OWNED BY public.reflask_users.id;


--
-- Name: reflask_posts id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reflask_posts ALTER COLUMN id SET DEFAULT nextval('public.reflask_posts_id_seq'::regclass);


--
-- Name: reflask_users id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reflask_users ALTER COLUMN id SET DEFAULT nextval('public.reflask_users_id_seq'::regclass);


--
-- Data for Name: reflask_posts; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.reflask_posts (id, title, content) FROM stdin;
4	Flask Web App	The Flask Web App is responsible for the database, migrations, and post lifecycle. In addition, local or OAuth2 registration is provided, and only logged in users can create, edit or delete posts.\r\n<div class="text-center"><a href="https://flask.local.projectscapa.com"  target="_blank" rel="noopener noreferrer">Web  App</a></div>
2	Flask API Service	The Flask API provides a RESTful API for Posts at <pre>/v2/posts</pre><pre>/v2/posts/&lt;id&gt;</pre>and implements <pre>/time</pre> as a health indicator.\r\n<div class="text-center"><a href="https://service.local.projectscapa.com/v2/posts"  target="_blank" rel="noopener noreferrer">API</a></div>
5	Docker Containers	<div style='padding-top:30px;'>\r\nTo deploy the application stack run <pre>make all</pre> Creates networks, volumes, builds containers, and starts services.\r\n</div>\r\n<ul><li>Postgres</li><li>NGinx proxy ssl</li><li>Api</li><li>App</li><li>React</li><li>Flask - Requirements</li></ul>
1	Flask and React	The Reflask platform includes <ul><li>Flask API for a Blog</li><li>Flask UI for Posting</li><li>React Frontend for Browsing</li><li>Postgres Database</li><li>NGinx Proxy SSL</li></ul>\r\nImplemented in Docker.
3	React UI	This colourful CardStack is built on React 16.8. The cards are collected from the Flask API Service @ <pre>/v2/posts</pre>
\.


--
-- Data for Name: reflask_users; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.reflask_users (id, google, username, email, created, bio, avatar, admin, password_hash) FROM stdin;
1	\N	GMcD	gary.macdonald@projectscapa.com	2020-09-06 10:08:25.821027	\N	\N	f	pbkdf2:sha256:150000$rIXIOL7E$012d848b9a7657ca05c36bb2337ca0b01225914e959c9c51e4588492384677b0
2	114709824829358339549	Gary	social.viral@gmail.com	2020-09-06 15:44:24.036454	\N	https://lh3.googleusercontent.com/a-/AOh14GjlYXSMpCJ8jzCWDGhSifCwYThzVx5Wx_YtuH4lUQ	f	\N
3	116348602891212387108	Project	project.scapa@gmail.com	2020-09-07 08:54:35.317081	\N	https://lh6.googleusercontent.com/-flGZ-L4iiEI/AAAAAAAAAAI/AAAAAAAAAAA/AMZuucmyaFJSxXN68SX-JmhsHI6txqPpdQ/photo.jpg	f	\N
\.


--
-- Name: reflask_posts_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.reflask_posts_id_seq', 5, true);


--
-- Name: reflask_users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.reflask_users_id_seq', 3, true);


--
-- Name: reflask_posts reflask_posts_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reflask_posts
    ADD CONSTRAINT reflask_posts_pkey PRIMARY KEY (id);


--
-- Name: reflask_posts reflask_posts_title_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reflask_posts
    ADD CONSTRAINT reflask_posts_title_key UNIQUE (title);


--
-- Name: reflask_users reflask_users_google_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reflask_users
    ADD CONSTRAINT reflask_users_google_key UNIQUE (google);


--
-- Name: reflask_users reflask_users_password_hash_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reflask_users
    ADD CONSTRAINT reflask_users_password_hash_key UNIQUE (password_hash);


--
-- Name: reflask_users reflask_users_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reflask_users
    ADD CONSTRAINT reflask_users_pkey PRIMARY KEY (id);


--
-- Name: reflask_users reflask_users_username_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reflask_users
    ADD CONSTRAINT reflask_users_username_key UNIQUE (username);


--
-- Name: ix_reflask_users_email; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX ix_reflask_users_email ON public.reflask_users USING btree (email);


--
-- PostgreSQL database dump complete
--

