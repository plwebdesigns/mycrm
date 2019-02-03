--
-- PostgreSQL database dump
--

-- Dumped from database version 10.5
-- Dumped by pg_dump version 10.5

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: task_manager_tasks; Type: TABLE; Schema: public; Owner: paul
--

CREATE TABLE public.task_manager_tasks (
    id integer NOT NULL,
    status character varying(100) NOT NULL,
    department character varying(100) NOT NULL,
    date_created date NOT NULL,
    date_due date NOT NULL,
    summary character varying(500),
    attachment character varying(100),
    client_id integer NOT NULL,
    employee_id integer NOT NULL
);


ALTER TABLE public.task_manager_tasks OWNER TO paul;

--
-- Name: task_manager_tasks_id_seq; Type: SEQUENCE; Schema: public; Owner: paul
--

CREATE SEQUENCE public.task_manager_tasks_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.task_manager_tasks_id_seq OWNER TO paul;

--
-- Name: task_manager_tasks_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: paul
--

ALTER SEQUENCE public.task_manager_tasks_id_seq OWNED BY public.task_manager_tasks.id;


--
-- Name: task_manager_tasks id; Type: DEFAULT; Schema: public; Owner: paul
--

ALTER TABLE ONLY public.task_manager_tasks ALTER COLUMN id SET DEFAULT nextval('public.task_manager_tasks_id_seq'::regclass);


--
-- Data for Name: task_manager_tasks; Type: TABLE DATA; Schema: public; Owner: paul
--

COPY public.task_manager_tasks (id, status, department, date_created, date_due, summary, attachment, client_id, employee_id) FROM stdin;
202	processing	Human Resources	2018-12-16	2019-02-03	\N	\N	71	68
203	completed	Research	2018-12-25	2019-02-21	Proin at turpis a pede posuere nonummy. Integer non velit.	\N	60	64
204	completed	Sales	2018-09-11	2019-02-09	\N	\N	70	62
205	processing	Research	2018-05-01	2019-02-05	\N	\N	70	64
206	completed	Human Resources	2018-03-17	2019-03-02	\N	\N	63	64
208	processing	Research	2018-11-27	2019-02-17	Donec semper sapien a libero.	\N	60	61
209	research	Human Resources	2018-11-07	2019-03-06	\N	\N	64	61
210	completed	Management	2018-11-29	2019-03-15	\N	\N	61	60
211	processing	Management	2018-02-24	2019-03-26	Praesent lectus.	\N	60	71
212	processing	Human Resources	2018-11-06	2019-02-01	\N	\N	60	67
213	processing	Research	2018-06-19	2019-02-02	Lorem ipsum dolor sit amet, consectetuer adipiscing elit.	\N	73	61
214	needs attention	Management	2018-01-23	2019-03-20	Suspendisse potenti.	\N	64	61
215	processing	Management	2018-12-12	2019-02-20	\N	\N	61	61
217	processing	Processing	2018-11-26	2019-02-04	Cras mi pede, malesuada in, imperdiet et, commodo vulputate, justo. In blandit ultrices enim. Lorem ipsum dolor sit amet, consectetuer adipiscing elit.	\N	66	72
218	needs attention	Research	2018-06-09	2019-02-20	Morbi a ipsum.	\N	72	73
219	needs attention	Human Resources	2018-12-17	2019-02-20	Proin eu mi. Nulla ac enim. In tempor, turpis nec euismod scelerisque, quam turpis adipiscing lorem, vitae mattis nibh ligula nec sem.	\N	65	68
220	completed	Management	2018-07-07	2019-03-13	Vestibulum rutrum rutrum neque.	\N	66	60
221	needs attention	Processing	2018-02-02	2019-03-25	Nunc nisl. Duis bibendum, felis sed interdum venenatis, turpis enim blandit mi, in porttitor pede justo eu massa. Donec dapibus.	\N	63	74
222	research	Sales	2018-11-03	2019-03-23	\N	\N	63	67
223	processing	Research	2018-03-26	2019-03-28	\N	\N	74	68
224	completed	Management	2018-08-29	2019-03-14	\N	\N	68	65
225	research	Research	2018-05-17	2019-02-06	Nullam sit amet turpis elementum ligula vehicula consequat. Morbi a ipsum.	\N	66	60
226	needs attention	Sales	2018-10-27	2019-02-16	Suspendisse ornare consequat lectus.	\N	73	66
227	processing	Human Resources	2018-02-05	2019-02-07	\N	\N	66	69
228	processing	Human Resources	2018-05-04	2019-02-11	\N	\N	66	67
229	completed	Sales	2018-06-11	2019-02-02	Etiam faucibus cursus urna. Ut tellus. Nulla ut erat id mauris vulputate elementum.	\N	61	63
230	needs attention	Research	2018-06-26	2019-02-11	Praesent blandit.	\N	71	63
231	research	Processing	2018-03-13	2019-02-14	Donec diam neque, vestibulum eget, vulputate ut, ultrices vel, augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec pharetra, magna vestibulum aliquet ultrices, erat tortor sollicitudin mi, sit amet lobortis sapien sapien non mi. Integer ac neque.	\N	73	64
232	completed	Management	2018-07-19	2019-03-03	\N	\N	71	64
233	research	Processing	2018-11-11	2019-02-11	Phasellus id sapien in sapien iaculis congue. Vivamus metus arcu, adipiscing molestie, hendrerit at, vulputate vitae, nisl.	\N	70	65
234	completed	Processing	2018-06-14	2019-02-11	Curabitur in libero ut massa volutpat convallis. Morbi odio odio, elementum eu, interdum eu, tincidunt in, leo. Maecenas pulvinar lobortis est.	\N	71	74
235	needs attention	Human Resources	2018-07-21	2019-03-13	Nunc purus.	\N	69	62
236	research	Human Resources	2018-05-11	2019-02-23	Nullam varius. Nulla facilisi.	\N	63	65
237	processing	Sales	2018-01-11	2019-03-15	Nullam sit amet turpis elementum ligula vehicula consequat.	\N	64	65
238	completed	Management	2018-11-20	2019-03-25	Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Mauris viverra diam vitae quam.	\N	74	60
239	needs attention	Research	2018-11-22	2019-02-21	\N	\N	73	74
240	needs attention	Management	2018-04-18	2019-03-15	Phasellus id sapien in sapien iaculis congue.	\N	71	61
241	processing	Sales	2018-08-28	2019-02-21	\N	\N	74	70
242	needs attention	Processing	2018-01-14	2019-02-07	\N	\N	72	67
243	needs attention	Research	2018-09-23	2019-03-21	Vivamus in felis eu sapien cursus vestibulum. Proin eu mi. Nulla ac enim.	\N	64	71
244	completed	Processing	2018-08-11	2019-03-03	Suspendisse potenti. In eleifend quam a odio.	\N	67	71
245	research	Processing	2018-06-04	2019-03-03	Duis bibendum, felis sed interdum venenatis, turpis enim blandit mi, in porttitor pede justo eu massa. Donec dapibus.	\N	74	73
246	completed	Research	2018-06-20	2019-02-14	Aliquam quis turpis eget elit sodales scelerisque. Mauris sit amet eros.	\N	68	62
247	research	Sales	2018-10-14	2019-02-08	\N	\N	74	64
248	needs attention	Processing	2018-09-27	2019-03-01	Aliquam non mauris.	\N	62	60
249	research	Processing	2018-07-31	2019-02-20	Suspendisse accumsan tortor quis turpis.	\N	68	68
250	research	Research	2018-04-07	2019-02-07	\N	\N	75	66
251	needs attention	Management	2018-02-02	2019-02-14	Proin eu mi. Nulla ac enim. In tempor, turpis nec euismod scelerisque, quam turpis adipiscing lorem, vitae mattis nibh ligula nec sem.	\N	60	64
252	processing	Sales	2018-11-01	2019-02-17	\N	\N	62	60
253	completed	Research	2018-09-04	2019-02-27	\N	\N	62	68
254	completed	Sales	2018-06-22	2019-02-19	Cras non velit nec nisi vulputate nonummy. Maecenas tincidunt lacus at velit. Vivamus vel nulla eget eros elementum pellentesque.	\N	62	66
255	completed	Research	2018-03-25	2019-02-28	\N	\N	68	67
256	needs attention	Human Resources	2018-09-08	2019-02-25	\N	\N	67	67
257	needs attention	Human Resources	2018-11-20	2019-02-22	Curabitur at ipsum ac tellus semper interdum. Mauris ullamcorper purus sit amet nulla.	\N	72	65
258	research	Human Resources	2018-10-29	2019-02-25	\N	\N	73	70
259	research	Management	2018-10-12	2019-03-10	Donec odio justo, sollicitudin ut, suscipit a, feugiat et, eros. Vestibulum ac est lacinia nisi venenatis tristique.	\N	68	61
260	research	Human Resources	2018-04-18	2019-02-26	Cras mi pede, malesuada in, imperdiet et, commodo vulputate, justo.	\N	66	67
261	needs attention	Processing	2018-09-26	2019-02-17	Morbi a ipsum.	\N	74	73
262	completed	Sales	2018-03-03	2019-02-28	\N	\N	73	64
216	processing	Human Resources	2019-01-07	2019-03-24	This is a fantastic job paul!!		73	60
207	attention	Human Resources	2019-01-07	2019-02-21	Aliquam erat volutpat.		60	68
263	needs attention	Human Resources	2018-11-01	2019-02-12	In hac habitasse platea dictumst. Morbi vestibulum, velit id pretium iaculis, diam erat fermentum justo, nec condimentum neque sapien placerat ante. Nulla justo.	\N	65	65
264	research	Research	2018-09-06	2019-02-20	\N	\N	65	71
265	research	Research	2018-11-09	2019-02-07	Maecenas tristique, est et tempus semper, est quam pharetra magna, ac consequat metus sapien ut nunc. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Mauris viverra diam vitae quam. Suspendisse potenti.	\N	69	66
266	processing	Research	2018-09-04	2019-02-05	\N	\N	63	61
267	research	Sales	2018-08-23	2019-03-14	\N	\N	60	63
268	needs attention	Management	2018-06-30	2019-03-01	Phasellus sit amet erat. Nulla tempus. Vivamus in felis eu sapien cursus vestibulum.	\N	64	70
269	needs attention	Processing	2018-09-26	2019-03-10	Duis at velit eu est congue elementum. In hac habitasse platea dictumst.	\N	73	61
270	research	Processing	2018-06-20	2019-03-09	Sed ante. Vivamus tortor. Duis mattis egestas metus.	\N	74	67
271	research	Human Resources	2018-09-06	2019-02-11	Morbi quis tortor id nulla ultrices aliquet. Maecenas leo odio, condimentum id, luctus nec, molestie sed, justo. Pellentesque viverra pede ac diam.	\N	62	61
272	research	Research	2018-09-19	2019-02-28	Donec vitae nisi. Nam ultrices, libero non mattis pulvinar, nulla pede ullamcorper augue, a suscipit nulla elit ac nulla. Sed vel enim sit amet nunc viverra dapibus.	\N	60	71
273	research	Human Resources	2018-10-09	2019-03-07	Donec odio justo, sollicitudin ut, suscipit a, feugiat et, eros. Vestibulum ac est lacinia nisi venenatis tristique. Fusce congue, diam id ornare imperdiet, sapien urna pretium nisl, ut volutpat sapien arcu sed augue.	\N	70	71
274	completed	Research	2018-01-16	2019-02-08	Nulla nisl. Nunc nisl. Duis bibendum, felis sed interdum venenatis, turpis enim blandit mi, in porttitor pede justo eu massa.	\N	70	64
275	processing	Research	2018-11-12	2019-03-16	\N	\N	74	70
276	completed	Sales	2018-03-23	2019-03-27	Phasellus id sapien in sapien iaculis congue. Vivamus metus arcu, adipiscing molestie, hendrerit at, vulputate vitae, nisl.	\N	67	68
277	research	Research	2018-04-06	2019-03-06	\N	\N	71	67
278	completed	Research	2018-08-24	2019-02-05	Cras mi pede, malesuada in, imperdiet et, commodo vulputate, justo. In blandit ultrices enim. Lorem ipsum dolor sit amet, consectetuer adipiscing elit.	\N	65	67
279	research	Research	2018-12-16	2019-03-02	Donec ut dolor. Morbi vel lectus in quam fringilla rhoncus. Mauris enim leo, rhoncus sed, vestibulum sit amet, cursus id, turpis.	\N	70	73
280	needs attention	Human Resources	2018-12-24	2019-03-24	Quisque erat eros, viverra eget, congue eget, semper rutrum, nulla. Nunc purus.	\N	71	69
281	processing	Human Resources	2018-02-15	2019-02-25	\N	\N	65	73
282	needs attention	Research	2018-01-17	2019-03-26	Nulla mollis molestie lorem. Quisque ut erat. Curabitur gravida nisi at nibh.	\N	72	62
283	completed	Sales	2018-05-07	2019-02-24	Maecenas rhoncus aliquam lacus. Morbi quis tortor id nulla ultrices aliquet.	\N	63	74
284	research	Research	2018-10-03	2019-03-01	Maecenas rhoncus aliquam lacus. Morbi quis tortor id nulla ultrices aliquet.	\N	68	65
285	processing	Human Resources	2018-01-25	2019-02-16	Nam congue, risus semper porta volutpat, quam pede lobortis ligula, sit amet eleifend pede libero quis orci.	\N	71	64
286	processing	Research	2018-08-10	2019-02-07	Aenean fermentum. Donec ut mauris eget massa tempor convallis.	\N	71	74
287	research	Management	2018-04-30	2019-02-02	\N	\N	66	66
288	research	Processing	2018-08-08	2019-03-25	Duis mattis egestas metus. Aenean fermentum. Donec ut mauris eget massa tempor convallis.	\N	75	61
289	research	Research	2018-12-22	2019-02-08	Proin risus.	\N	66	63
290	research	Research	2018-05-22	2019-02-20	Nam congue, risus semper porta volutpat, quam pede lobortis ligula, sit amet eleifend pede libero quis orci. Nullam molestie nibh in lectus.	\N	68	68
291	processing	Human Resources	2018-03-22	2019-03-06	Cras pellentesque volutpat dui. Maecenas tristique, est et tempus semper, est quam pharetra magna, ac consequat metus sapien ut nunc. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Mauris viverra diam vitae quam.	\N	75	63
292	completed	Sales	2018-12-29	2019-03-16	Sed vel enim sit amet nunc viverra dapibus.	\N	71	69
293	completed	Human Resources	2018-10-07	2019-02-17	Curabitur at ipsum ac tellus semper interdum. Mauris ullamcorper purus sit amet nulla.	\N	72	60
294	needs attention	Sales	2018-08-15	2019-03-03	Cras pellentesque volutpat dui. Maecenas tristique, est et tempus semper, est quam pharetra magna, ac consequat metus sapien ut nunc.	\N	68	60
295	research	Processing	2018-09-02	2019-02-19	Aliquam erat volutpat. In congue. Etiam justo.	\N	62	72
296	research	Human Resources	2018-01-25	2019-03-25	Vestibulum sed magna at nunc commodo placerat. Praesent blandit.	\N	64	63
297	research	Management	2018-10-09	2019-03-24	\N	\N	61	65
298	processing	Human Resources	2018-04-30	2019-03-10	In hac habitasse platea dictumst. Morbi vestibulum, velit id pretium iaculis, diam erat fermentum justo, nec condimentum neque sapien placerat ante. Nulla justo.	\N	63	61
299	needs attention	Management	2018-08-07	2019-03-11	\N	\N	66	73
300	research	Processing	2018-01-15	2019-02-22	\N	\N	69	61
301	attention	Telemarketing	2019-01-08	2019-12-03			13	7
302	research	Research	2019-01-09	2019-02-01	This is a test to see how it looks		3	20
\.


--
-- Name: task_manager_tasks_id_seq; Type: SEQUENCE SET; Schema: public; Owner: paul
--

SELECT pg_catalog.setval('public.task_manager_tasks_id_seq', 302, true);


--
-- Name: task_manager_tasks task_manager_tasks_pkey; Type: CONSTRAINT; Schema: public; Owner: paul
--

ALTER TABLE ONLY public.task_manager_tasks
    ADD CONSTRAINT task_manager_tasks_pkey PRIMARY KEY (id);


--
-- Name: task_manager_tasks_client_id_42cc6b0d; Type: INDEX; Schema: public; Owner: paul
--

CREATE INDEX task_manager_tasks_client_id_42cc6b0d ON public.task_manager_tasks USING btree (client_id);


--
-- Name: task_manager_tasks_employee_id_70d4e2c8; Type: INDEX; Schema: public; Owner: paul
--

CREATE INDEX task_manager_tasks_employee_id_70d4e2c8 ON public.task_manager_tasks USING btree (employee_id);


--
-- Name: task_manager_tasks task_manager_tasks_client_id_42cc6b0d_fk_clients_client_id; Type: FK CONSTRAINT; Schema: public; Owner: paul
--

ALTER TABLE ONLY public.task_manager_tasks
    ADD CONSTRAINT task_manager_tasks_client_id_42cc6b0d_fk_clients_client_id FOREIGN KEY (client_id) REFERENCES public.clients_client(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: task_manager_tasks task_manager_tasks_employee_id_70d4e2c8_fk_employees; Type: FK CONSTRAINT; Schema: public; Owner: paul
--

ALTER TABLE ONLY public.task_manager_tasks
    ADD CONSTRAINT task_manager_tasks_employee_id_70d4e2c8_fk_employees FOREIGN KEY (employee_id) REFERENCES public.employees_employee(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

