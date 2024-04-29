--
-- PostgreSQL database dump
--

-- Dumped from database version 15.2
-- Dumped by pg_dump version 15.2

-- Started on 2024-04-30 00:19:06

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

--
-- TOC entry 3924 (class 0 OID 81665)
-- Dependencies: 221
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.auth_group (id, name) FROM stdin;
1	Moderators
2	Editors
\.


--
-- TOC entry 3920 (class 0 OID 81651)
-- Dependencies: 217
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	wagtailcore	page
2	home	homepage
3	wagtailadmin	admin
4	wagtailcore	groupapprovaltask
5	wagtailcore	locale
6	wagtailcore	site
7	wagtailcore	modellogentry
8	wagtailcore	collectionviewrestriction
9	wagtailcore	collection
10	wagtailcore	groupcollectionpermission
11	wagtailcore	referenceindex
12	wagtailcore	revision
13	wagtailcore	grouppagepermission
14	wagtailcore	pageviewrestriction
15	wagtailcore	workflowpage
16	wagtailcore	workflowcontenttype
17	wagtailcore	workflowtask
18	wagtailcore	task
19	wagtailcore	workflow
20	wagtailcore	workflowstate
21	wagtailcore	taskstate
22	wagtailcore	pagelogentry
23	wagtailcore	comment
24	wagtailcore	commentreply
25	wagtailcore	pagesubscription
26	wagtaildocs	document
27	wagtailimages	image
28	wagtailforms	formsubmission
29	wagtailredirects	redirect
30	wagtailembeds	embed
31	wagtailusers	userprofile
32	wagtaildocs	uploadeddocument
33	wagtailimages	rendition
34	wagtailimages	uploadedimage
35	wagtailsearch	indexentry
36	taggit	tag
37	taggit	taggeditem
38	admin	logentry
39	auth	permission
40	auth	group
41	auth	user
42	contenttypes	contenttype
43	sessions	session
\.


--
-- TOC entry 3922 (class 0 OID 81659)
-- Dependencies: 219
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can access Wagtail admin	3	access_admin
2	Can add locale	5	add_locale
3	Can change locale	5	change_locale
4	Can delete locale	5	delete_locale
5	Can view locale	5	view_locale
6	Can add site	6	add_site
7	Can change site	6	change_site
8	Can delete site	6	delete_site
9	Can view site	6	view_site
10	Can add model log entry	7	add_modellogentry
11	Can change model log entry	7	change_modellogentry
12	Can delete model log entry	7	delete_modellogentry
13	Can view model log entry	7	view_modellogentry
14	Can add collection view restriction	8	add_collectionviewrestriction
15	Can change collection view restriction	8	change_collectionviewrestriction
16	Can delete collection view restriction	8	delete_collectionviewrestriction
17	Can view collection view restriction	8	view_collectionviewrestriction
18	Can add collection	9	add_collection
19	Can change collection	9	change_collection
20	Can delete collection	9	delete_collection
21	Can view collection	9	view_collection
22	Can add group collection permission	10	add_groupcollectionpermission
23	Can change group collection permission	10	change_groupcollectionpermission
24	Can delete group collection permission	10	delete_groupcollectionpermission
25	Can view group collection permission	10	view_groupcollectionpermission
26	Can add reference index	11	add_referenceindex
27	Can change reference index	11	change_referenceindex
28	Can delete reference index	11	delete_referenceindex
29	Can view reference index	11	view_referenceindex
30	Can add page	1	add_page
31	Can change page	1	change_page
32	Can delete page	1	delete_page
33	Can view page	1	view_page
34	Delete pages with children	1	bulk_delete_page
35	Lock/unlock pages you've locked	1	lock_page
36	Publish any page	1	publish_page
37	Unlock any page	1	unlock_page
38	Can add revision	12	add_revision
39	Can change revision	12	change_revision
40	Can delete revision	12	delete_revision
41	Can view revision	12	view_revision
42	Can add group page permission	13	add_grouppagepermission
43	Can change group page permission	13	change_grouppagepermission
44	Can delete group page permission	13	delete_grouppagepermission
45	Can view group page permission	13	view_grouppagepermission
46	Can add page view restriction	14	add_pageviewrestriction
47	Can change page view restriction	14	change_pageviewrestriction
48	Can delete page view restriction	14	delete_pageviewrestriction
49	Can view page view restriction	14	view_pageviewrestriction
50	Can add workflow page	15	add_workflowpage
51	Can change workflow page	15	change_workflowpage
52	Can delete workflow page	15	delete_workflowpage
53	Can view workflow page	15	view_workflowpage
54	Can add workflow content type	16	add_workflowcontenttype
55	Can change workflow content type	16	change_workflowcontenttype
56	Can delete workflow content type	16	delete_workflowcontenttype
57	Can view workflow content type	16	view_workflowcontenttype
58	Can add workflow task order	17	add_workflowtask
59	Can change workflow task order	17	change_workflowtask
60	Can delete workflow task order	17	delete_workflowtask
61	Can view workflow task order	17	view_workflowtask
62	Can add task	18	add_task
63	Can change task	18	change_task
64	Can delete task	18	delete_task
65	Can view task	18	view_task
66	Can add workflow	19	add_workflow
67	Can change workflow	19	change_workflow
68	Can delete workflow	19	delete_workflow
69	Can view workflow	19	view_workflow
70	Can add Group approval task	4	add_groupapprovaltask
71	Can change Group approval task	4	change_groupapprovaltask
72	Can delete Group approval task	4	delete_groupapprovaltask
73	Can view Group approval task	4	view_groupapprovaltask
74	Can add Workflow state	20	add_workflowstate
75	Can change Workflow state	20	change_workflowstate
76	Can delete Workflow state	20	delete_workflowstate
77	Can view Workflow state	20	view_workflowstate
78	Can add Task state	21	add_taskstate
79	Can change Task state	21	change_taskstate
80	Can delete Task state	21	delete_taskstate
81	Can view Task state	21	view_taskstate
82	Can add page log entry	22	add_pagelogentry
83	Can change page log entry	22	change_pagelogentry
84	Can delete page log entry	22	delete_pagelogentry
85	Can view page log entry	22	view_pagelogentry
86	Can add comment	23	add_comment
87	Can change comment	23	change_comment
88	Can delete comment	23	delete_comment
89	Can view comment	23	view_comment
90	Can add comment reply	24	add_commentreply
91	Can change comment reply	24	change_commentreply
92	Can delete comment reply	24	delete_commentreply
93	Can view comment reply	24	view_commentreply
94	Can add page subscription	25	add_pagesubscription
95	Can change page subscription	25	change_pagesubscription
96	Can delete page subscription	25	delete_pagesubscription
97	Can view page subscription	25	view_pagesubscription
98	Can add document	26	add_document
99	Can change document	26	change_document
100	Can delete document	26	delete_document
101	Can choose document	26	choose_document
102	Can add image	27	add_image
103	Can change image	27	change_image
104	Can delete image	27	delete_image
105	Can choose image	27	choose_image
106	Can add home page	2	add_homepage
107	Can change home page	2	change_homepage
108	Can delete home page	2	delete_homepage
109	Can view home page	2	view_homepage
110	Can add form submission	28	add_formsubmission
111	Can change form submission	28	change_formsubmission
112	Can delete form submission	28	delete_formsubmission
113	Can view form submission	28	view_formsubmission
114	Can add redirect	29	add_redirect
115	Can change redirect	29	change_redirect
116	Can delete redirect	29	delete_redirect
117	Can view redirect	29	view_redirect
118	Can add embed	30	add_embed
119	Can change embed	30	change_embed
120	Can delete embed	30	delete_embed
121	Can view embed	30	view_embed
122	Can add user profile	31	add_userprofile
123	Can change user profile	31	change_userprofile
124	Can delete user profile	31	delete_userprofile
125	Can view user profile	31	view_userprofile
126	Can view document	26	view_document
127	Can add uploaded document	32	add_uploadeddocument
128	Can change uploaded document	32	change_uploadeddocument
129	Can delete uploaded document	32	delete_uploadeddocument
130	Can view uploaded document	32	view_uploadeddocument
131	Can view image	27	view_image
132	Can add rendition	33	add_rendition
133	Can change rendition	33	change_rendition
134	Can delete rendition	33	delete_rendition
135	Can view rendition	33	view_rendition
136	Can add uploaded image	34	add_uploadedimage
137	Can change uploaded image	34	change_uploadedimage
138	Can delete uploaded image	34	delete_uploadedimage
139	Can view uploaded image	34	view_uploadedimage
140	Can add index entry	35	add_indexentry
141	Can change index entry	35	change_indexentry
142	Can delete index entry	35	delete_indexentry
143	Can view index entry	35	view_indexentry
144	Can add tag	36	add_tag
145	Can change tag	36	change_tag
146	Can delete tag	36	delete_tag
147	Can view tag	36	view_tag
148	Can add tagged item	37	add_taggeditem
149	Can change tagged item	37	change_taggeditem
150	Can delete tagged item	37	delete_taggeditem
151	Can view tagged item	37	view_taggeditem
152	Can add log entry	38	add_logentry
153	Can change log entry	38	change_logentry
154	Can delete log entry	38	delete_logentry
155	Can view log entry	38	view_logentry
156	Can add permission	39	add_permission
157	Can change permission	39	change_permission
158	Can delete permission	39	delete_permission
159	Can view permission	39	view_permission
160	Can add group	40	add_group
161	Can change group	40	change_group
162	Can delete group	40	delete_group
163	Can view group	40	view_group
164	Can add user	41	add_user
165	Can change user	41	change_user
166	Can delete user	41	delete_user
167	Can view user	41	view_user
168	Can add content type	42	add_contenttype
169	Can change content type	42	change_contenttype
170	Can delete content type	42	delete_contenttype
171	Can view content type	42	view_contenttype
172	Can add session	43	add_session
173	Can change session	43	change_session
174	Can delete session	43	delete_session
175	Can view session	43	view_session
\.


--
-- TOC entry 3926 (class 0 OID 81673)
-- Dependencies: 223
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
1	1	1
2	2	1
3	1	98
4	1	99
5	1	100
6	2	98
7	2	99
8	2	100
9	1	101
10	2	101
11	1	104
12	1	102
13	1	103
14	2	104
15	2	102
16	2	103
17	1	105
18	2	105
\.


--
-- TOC entry 3928 (class 0 OID 81679)
-- Dependencies: 225
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$600000$DgQf91xZtfUusBBOWBKuH6$0IEVWQT9Yfq2cN5RQEllJ5HFlHyAhdKv5FUB0VStPzA=	\N	t	ringaz			ringazm@gmail.com	t	t	2024-04-26 00:46:26.643416+02
\.


--
-- TOC entry 3930 (class 0 OID 81687)
-- Dependencies: 227
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- TOC entry 3932 (class 0 OID 81693)
-- Dependencies: 229
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- TOC entry 3934 (class 0 OID 81751)
-- Dependencies: 231
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
\.


--
-- TOC entry 3918 (class 0 OID 81643)
-- Dependencies: 215
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2024-04-26 00:44:49.740725+02
2	auth	0001_initial	2024-04-26 00:44:50.786541+02
3	admin	0001_initial	2024-04-26 00:44:50.997467+02
4	admin	0002_logentry_remove_auto_add	2024-04-26 00:44:51.012717+02
5	admin	0003_logentry_add_action_flag_choices	2024-04-26 00:44:51.033528+02
6	contenttypes	0002_remove_content_type_name	2024-04-26 00:44:51.069285+02
7	auth	0002_alter_permission_name_max_length	2024-04-26 00:44:51.086698+02
8	auth	0003_alter_user_email_max_length	2024-04-26 00:44:51.103938+02
9	auth	0004_alter_user_username_opts	2024-04-26 00:44:51.121137+02
10	auth	0005_alter_user_last_login_null	2024-04-26 00:44:51.137468+02
11	auth	0006_require_contenttypes_0002	2024-04-26 00:44:51.142468+02
12	auth	0007_alter_validators_add_error_messages	2024-04-26 00:44:51.159779+02
13	auth	0008_alter_user_username_max_length	2024-04-26 00:44:51.208447+02
14	auth	0009_alter_user_last_name_max_length	2024-04-26 00:44:51.252241+02
15	auth	0010_alter_group_name_max_length	2024-04-26 00:44:51.272053+02
16	auth	0011_update_proxy_permissions	2024-04-26 00:44:51.307185+02
17	auth	0012_alter_user_first_name_max_length	2024-04-26 00:44:51.338736+02
18	wagtailcore	0001_initial	2024-04-26 00:44:52.493717+02
19	wagtailcore	0002_initial_data	2024-04-26 00:44:52.506061+02
20	wagtailcore	0003_add_uniqueness_constraint_on_group_page_permission	2024-04-26 00:44:52.509492+02
21	wagtailcore	0004_page_locked	2024-04-26 00:44:52.512495+02
22	wagtailcore	0005_add_page_lock_permission_to_moderators	2024-04-26 00:44:52.515493+02
23	wagtailcore	0006_add_lock_page_permission	2024-04-26 00:44:52.5187+02
24	wagtailcore	0007_page_latest_revision_created_at	2024-04-26 00:44:52.522701+02
25	wagtailcore	0008_populate_latest_revision_created_at	2024-04-26 00:44:52.525129+02
26	wagtailcore	0009_remove_auto_now_add_from_pagerevision_created_at	2024-04-26 00:44:52.529011+02
27	wagtailcore	0010_change_page_owner_to_null_on_delete	2024-04-26 00:44:52.53219+02
28	wagtailcore	0011_page_first_published_at	2024-04-26 00:44:52.535183+02
29	wagtailcore	0012_extend_page_slug_field	2024-04-26 00:44:52.538182+02
30	wagtailcore	0013_update_golive_expire_help_text	2024-04-26 00:44:52.541479+02
31	wagtailcore	0014_add_verbose_name	2024-04-26 00:44:52.54448+02
32	wagtailcore	0015_add_more_verbose_names	2024-04-26 00:44:52.548442+02
33	wagtailcore	0016_change_page_url_path_to_text_field	2024-04-26 00:44:52.551621+02
34	wagtailcore	0017_change_edit_page_permission_description	2024-04-26 00:44:52.570322+02
35	wagtailcore	0018_pagerevision_submitted_for_moderation_index	2024-04-26 00:44:52.668943+02
36	wagtailcore	0019_verbose_names_cleanup	2024-04-26 00:44:52.732948+02
37	wagtailcore	0020_add_index_on_page_first_published_at	2024-04-26 00:44:52.782901+02
38	wagtailcore	0021_capitalizeverbose	2024-04-26 00:44:53.177164+02
39	wagtailcore	0022_add_site_name	2024-04-26 00:44:53.235566+02
40	wagtailcore	0023_alter_page_revision_on_delete_behaviour	2024-04-26 00:44:53.258145+02
41	wagtailcore	0024_collection	2024-04-26 00:44:53.423089+02
42	wagtailcore	0025_collection_initial_data	2024-04-26 00:44:53.448933+02
43	wagtailcore	0026_group_collection_permission	2024-04-26 00:44:53.679686+02
44	wagtailcore	0027_fix_collection_path_collation	2024-04-26 00:44:53.794871+02
45	wagtailcore	0024_alter_page_content_type_on_delete_behaviour	2024-04-26 00:44:53.835789+02
46	wagtailcore	0028_merge	2024-04-26 00:44:53.840418+02
47	wagtailcore	0029_unicode_slugfield_dj19	2024-04-26 00:44:53.860786+02
48	wagtailcore	0030_index_on_pagerevision_created_at	2024-04-26 00:44:53.919258+02
49	wagtailcore	0031_add_page_view_restriction_types	2024-04-26 00:44:54.174575+02
50	wagtailcore	0032_add_bulk_delete_page_permission	2024-04-26 00:44:54.193829+02
51	wagtailcore	0033_remove_golive_expiry_help_text	2024-04-26 00:44:54.231126+02
52	wagtailcore	0034_page_live_revision	2024-04-26 00:44:54.287656+02
53	wagtailcore	0035_page_last_published_at	2024-04-26 00:44:54.308487+02
54	wagtailcore	0036_populate_page_last_published_at	2024-04-26 00:44:54.343609+02
55	wagtailcore	0037_set_page_owner_editable	2024-04-26 00:44:54.385827+02
56	wagtailcore	0038_make_first_published_at_editable	2024-04-26 00:44:54.475522+02
57	wagtailcore	0039_collectionviewrestriction	2024-04-26 00:44:54.769353+02
58	wagtailcore	0040_page_draft_title	2024-04-26 00:44:54.825117+02
59	home	0001_initial	2024-04-26 00:44:54.889162+02
60	home	0002_create_homepage	2024-04-26 00:44:54.957662+02
61	sessions	0001_initial	2024-04-26 00:44:55.13417+02
62	taggit	0001_initial	2024-04-26 00:44:55.479705+02
63	taggit	0002_auto_20150616_2121	2024-04-26 00:44:55.524585+02
64	taggit	0003_taggeditem_add_unique_index	2024-04-26 00:44:55.58322+02
65	taggit	0004_alter_taggeditem_content_type_alter_taggeditem_tag	2024-04-26 00:44:55.651087+02
66	taggit	0005_auto_20220424_2025	2024-04-26 00:44:55.658638+02
67	taggit	0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx	2024-04-26 00:44:55.70047+02
68	wagtailadmin	0001_create_admin_access_permissions	2024-04-26 00:44:55.75003+02
69	wagtailadmin	0002_admin	2024-04-26 00:44:55.757579+02
70	wagtailadmin	0003_admin_managed	2024-04-26 00:44:55.798381+02
71	wagtailcore	0041_group_collection_permissions_verbose_name_plural	2024-04-26 00:44:55.81702+02
72	wagtailcore	0042_index_on_pagerevision_approved_go_live_at	2024-04-26 00:44:55.900289+02
73	wagtailcore	0043_lock_fields	2024-04-26 00:44:55.980582+02
74	wagtailcore	0044_add_unlock_grouppagepermission	2024-04-26 00:44:56.005004+02
75	wagtailcore	0045_assign_unlock_grouppagepermission	2024-04-26 00:44:56.042928+02
76	wagtailcore	0046_site_name_remove_null	2024-04-26 00:44:56.068688+02
77	wagtailcore	0047_add_workflow_models	2024-04-26 00:44:57.284167+02
78	wagtailcore	0048_add_default_workflows	2024-04-26 00:44:57.398474+02
79	wagtailcore	0049_taskstate_finished_by	2024-04-26 00:44:57.498728+02
80	wagtailcore	0050_workflow_rejected_to_needs_changes	2024-04-26 00:44:57.710488+02
81	wagtailcore	0051_taskstate_comment	2024-04-26 00:44:57.781637+02
82	wagtailcore	0052_pagelogentry	2024-04-26 00:44:58.127528+02
83	wagtailcore	0053_locale_model	2024-04-26 00:44:58.238841+02
84	wagtailcore	0054_initial_locale	2024-04-26 00:44:58.289433+02
85	wagtailcore	0055_page_locale_fields	2024-04-26 00:44:58.472435+02
86	wagtailcore	0056_page_locale_fields_populate	2024-04-26 00:44:58.537367+02
87	wagtailcore	0057_page_locale_fields_notnull	2024-04-26 00:44:58.635012+02
88	wagtailcore	0058_page_alias_of	2024-04-26 00:44:58.731367+02
89	wagtailcore	0059_apply_collection_ordering	2024-04-26 00:44:58.808483+02
90	wagtailcore	0060_fix_workflow_unique_constraint	2024-04-26 00:44:58.910731+02
91	wagtailcore	0061_change_promote_tab_helpt_text_and_verbose_names	2024-04-26 00:44:58.997709+02
92	wagtailcore	0062_comment_models_and_pagesubscription	2024-04-26 00:44:59.695614+02
93	wagtailcore	0063_modellogentry	2024-04-26 00:45:00.106774+02
94	wagtailcore	0064_log_timestamp_indexes	2024-04-26 00:45:00.229361+02
95	wagtailcore	0065_log_entry_uuid	2024-04-26 00:45:00.297992+02
96	wagtailcore	0066_collection_management_permissions	2024-04-26 00:45:00.378853+02
97	wagtailcore	0067_alter_pagerevision_content_json	2024-04-26 00:45:00.762888+02
98	wagtailcore	0068_log_entry_empty_object	2024-04-26 00:45:00.843451+02
99	wagtailcore	0069_log_entry_jsonfield	2024-04-26 00:45:01.752266+02
100	wagtailcore	0070_rename_pagerevision_revision	2024-04-26 00:45:02.492057+02
101	wagtailcore	0071_populate_revision_content_type	2024-04-26 00:45:02.549356+02
102	wagtailcore	0072_alter_revision_content_type_notnull	2024-04-26 00:45:02.65369+02
103	wagtailcore	0073_page_latest_revision	2024-04-26 00:45:02.739008+02
104	wagtailcore	0074_revision_object_str	2024-04-26 00:45:02.770535+02
105	wagtailcore	0075_populate_latest_revision_and_revision_object_str	2024-04-26 00:45:02.952331+02
106	wagtailcore	0076_modellogentry_revision	2024-04-26 00:45:03.029523+02
107	wagtailcore	0077_alter_revision_user	2024-04-26 00:45:03.077968+02
108	wagtailcore	0078_referenceindex	2024-04-26 00:45:03.3334+02
109	wagtailcore	0079_rename_taskstate_page_revision	2024-04-26 00:45:03.375985+02
110	wagtailcore	0080_generic_workflowstate	2024-04-26 00:45:03.940635+02
111	wagtailcore	0081_populate_workflowstate_content_type	2024-04-26 00:45:04.006175+02
112	wagtailcore	0082_alter_workflowstate_content_type_notnull	2024-04-26 00:45:04.116248+02
113	wagtailcore	0083_workflowcontenttype	2024-04-26 00:45:04.263572+02
114	wagtailcore	0084_add_default_page_permissions	2024-04-26 00:45:04.312522+02
115	wagtailcore	0085_add_grouppagepermission_permission	2024-04-26 00:45:04.494021+02
116	wagtailcore	0086_populate_grouppagepermission_permission	2024-04-26 00:45:04.726972+02
117	wagtailcore	0087_alter_grouppagepermission_unique_together_and_more	2024-04-26 00:45:04.923882+02
118	wagtailcore	0088_fix_log_entry_json_timestamps	2024-04-26 00:45:05.059909+02
119	wagtailcore	0089_log_entry_data_json_null_to_object	2024-04-26 00:45:05.14012+02
120	wagtailcore	0090_remove_grouppagepermission_permission_type	2024-04-26 00:45:05.280038+02
121	wagtailcore	0091_remove_revision_submitted_for_moderation	2024-04-26 00:45:05.317918+02
122	wagtaildocs	0001_initial	2024-04-26 00:45:05.465952+02
123	wagtaildocs	0002_initial_data	2024-04-26 00:45:05.536127+02
124	wagtaildocs	0003_add_verbose_names	2024-04-26 00:45:05.632071+02
125	wagtaildocs	0004_capitalizeverbose	2024-04-26 00:45:05.894578+02
126	wagtaildocs	0005_document_collection	2024-04-26 00:45:05.980981+02
127	wagtaildocs	0006_copy_document_permissions_to_collections	2024-04-26 00:45:06.052205+02
128	wagtaildocs	0005_alter_uploaded_by_user_on_delete_action	2024-04-26 00:45:06.102152+02
129	wagtaildocs	0007_merge	2024-04-26 00:45:06.107659+02
130	wagtaildocs	0008_document_file_size	2024-04-26 00:45:06.142976+02
131	wagtaildocs	0009_document_verbose_name_plural	2024-04-26 00:45:06.201819+02
132	wagtaildocs	0010_document_file_hash	2024-04-26 00:45:06.239455+02
133	wagtaildocs	0011_add_choose_permissions	2024-04-26 00:45:06.372223+02
134	wagtaildocs	0012_uploadeddocument	2024-04-26 00:45:06.510806+02
135	wagtailembeds	0001_initial	2024-04-26 00:45:06.619513+02
136	wagtailembeds	0002_add_verbose_names	2024-04-26 00:45:06.629925+02
137	wagtailembeds	0003_capitalizeverbose	2024-04-26 00:45:06.641975+02
138	wagtailembeds	0004_embed_verbose_name_plural	2024-04-26 00:45:06.652275+02
139	wagtailembeds	0005_specify_thumbnail_url_max_length	2024-04-26 00:45:06.663065+02
140	wagtailembeds	0006_add_embed_hash	2024-04-26 00:45:06.672066+02
141	wagtailembeds	0007_populate_hash	2024-04-26 00:45:06.727955+02
142	wagtailembeds	0008_allow_long_urls	2024-04-26 00:45:06.817172+02
143	wagtailembeds	0009_embed_cache_until	2024-04-26 00:45:06.893566+02
144	wagtailforms	0001_initial	2024-04-26 00:45:07.035659+02
145	wagtailforms	0002_add_verbose_names	2024-04-26 00:45:07.08138+02
146	wagtailforms	0003_capitalizeverbose	2024-04-26 00:45:07.12721+02
147	wagtailforms	0004_add_verbose_name_plural	2024-04-26 00:45:07.153035+02
148	wagtailforms	0005_alter_formsubmission_form_data	2024-04-26 00:45:07.264093+02
149	wagtailimages	0001_initial	2024-04-26 00:45:07.957063+02
150	wagtailimages	0002_initial_data	2024-04-26 00:45:07.961059+02
151	wagtailimages	0003_fix_focal_point_fields	2024-04-26 00:45:07.965061+02
152	wagtailimages	0004_make_focal_point_key_not_nullable	2024-04-26 00:45:07.96937+02
153	wagtailimages	0005_make_filter_spec_unique	2024-04-26 00:45:07.972711+02
154	wagtailimages	0006_add_verbose_names	2024-04-26 00:45:07.977675+02
155	wagtailimages	0007_image_file_size	2024-04-26 00:45:07.980635+02
156	wagtailimages	0008_image_created_at_index	2024-04-26 00:45:07.984634+02
157	wagtailimages	0009_capitalizeverbose	2024-04-26 00:45:07.988834+02
158	wagtailimages	0010_change_on_delete_behaviour	2024-04-26 00:45:07.992834+02
159	wagtailimages	0011_image_collection	2024-04-26 00:45:07.996461+02
160	wagtailimages	0012_copy_image_permissions_to_collections	2024-04-26 00:45:08.000354+02
161	wagtailimages	0013_make_rendition_upload_callable	2024-04-26 00:45:08.004354+02
162	wagtailimages	0014_add_filter_spec_field	2024-04-26 00:45:08.008692+02
163	wagtailimages	0015_fill_filter_spec_field	2024-04-26 00:45:08.012688+02
164	wagtailimages	0016_deprecate_rendition_filter_relation	2024-04-26 00:45:08.016725+02
165	wagtailimages	0017_reduce_focal_point_key_max_length	2024-04-26 00:45:08.019687+02
166	wagtailimages	0018_remove_rendition_filter	2024-04-26 00:45:08.023686+02
167	wagtailimages	0019_delete_filter	2024-04-26 00:45:08.027687+02
168	wagtailimages	0020_add-verbose-name	2024-04-26 00:45:08.032005+02
169	wagtailimages	0021_image_file_hash	2024-04-26 00:45:08.045003+02
170	wagtailimages	0022_uploadedimage	2024-04-26 00:45:08.168707+02
171	wagtailimages	0023_add_choose_permissions	2024-04-26 00:45:08.350528+02
172	wagtailimages	0024_index_image_file_hash	2024-04-26 00:45:08.458005+02
173	wagtailimages	0025_alter_image_file_alter_rendition_file	2024-04-26 00:45:08.513293+02
174	wagtailredirects	0001_initial	2024-04-26 00:45:08.815974+02
175	wagtailredirects	0002_add_verbose_names	2024-04-26 00:45:08.89664+02
176	wagtailredirects	0003_make_site_field_editable	2024-04-26 00:45:08.952672+02
177	wagtailredirects	0004_set_unique_on_path_and_site	2024-04-26 00:45:09.063591+02
178	wagtailredirects	0005_capitalizeverbose	2024-04-26 00:45:09.331132+02
179	wagtailredirects	0006_redirect_increase_max_length	2024-04-26 00:45:09.413436+02
180	wagtailredirects	0007_add_autocreate_fields	2024-04-26 00:45:09.487398+02
181	wagtailredirects	0008_add_verbose_name_plural	2024-04-26 00:45:09.517344+02
182	wagtailsearch	0001_initial	2024-04-26 00:45:10.256801+02
183	wagtailsearch	0002_add_verbose_names	2024-04-26 00:45:10.366672+02
184	wagtailsearch	0003_remove_editors_pick	2024-04-26 00:45:10.373632+02
185	wagtailsearch	0004_querydailyhits_verbose_name_plural	2024-04-26 00:45:10.393873+02
186	wagtailsearch	0005_create_indexentry	2024-04-26 00:45:10.579117+02
187	wagtailsearch	0006_customise_indexentry	2024-04-26 00:45:10.768196+02
188	wagtailsearch	0007_delete_editorspick	2024-04-26 00:45:10.800736+02
189	wagtailsearch	0008_remove_query_and_querydailyhits_models	2024-04-26 00:45:10.845321+02
190	wagtailusers	0001_initial	2024-04-26 00:45:10.97851+02
191	wagtailusers	0002_add_verbose_name_on_userprofile	2024-04-26 00:45:11.069785+02
192	wagtailusers	0003_add_verbose_names	2024-04-26 00:45:11.103097+02
193	wagtailusers	0004_capitalizeverbose	2024-04-26 00:45:11.297042+02
194	wagtailusers	0005_make_related_name_wagtail_specific	2024-04-26 00:45:11.354876+02
195	wagtailusers	0006_userprofile_prefered_language	2024-04-26 00:45:11.393137+02
196	wagtailusers	0007_userprofile_current_time_zone	2024-04-26 00:45:11.42766+02
197	wagtailusers	0008_userprofile_avatar	2024-04-26 00:45:11.4672+02
198	wagtailusers	0009_userprofile_verbose_name_plural	2024-04-26 00:45:11.501957+02
199	wagtailusers	0010_userprofile_updated_comments_notifications	2024-04-26 00:45:11.540207+02
200	wagtailusers	0011_userprofile_dismissibles	2024-04-26 00:45:11.610339+02
201	wagtailusers	0012_userprofile_theme	2024-04-26 00:45:11.647226+02
202	wagtailimages	0001_squashed_0021	2024-04-26 00:45:11.660221+02
203	wagtailcore	0001_squashed_0016_change_page_url_path_to_text_field	2024-04-26 00:45:11.671419+02
\.


--
-- TOC entry 3956 (class 0 OID 81993)
-- Dependencies: 253
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
\.


--
-- TOC entry 3980 (class 0 OID 82227)
-- Dependencies: 277
-- Data for Name: wagtailcore_locale; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_locale (id, language_code) FROM stdin;
1	en
\.


--
-- TOC entry 3940 (class 0 OID 81802)
-- Dependencies: 237
-- Data for Name: wagtailcore_revision; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_revision (id, created_at, content, approved_go_live_at, object_id, user_id, content_type_id, base_content_type_id, object_str) FROM stdin;
\.


--
-- TOC entry 3936 (class 0 OID 81780)
-- Dependencies: 233
-- Data for Name: wagtailcore_page; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_page (id, path, depth, numchild, title, slug, live, has_unpublished_changes, url_path, seo_title, show_in_menus, search_description, go_live_at, expire_at, expired, content_type_id, owner_id, locked, latest_revision_created_at, first_published_at, live_revision_id, last_published_at, draft_title, locked_at, locked_by_id, translation_key, locale_id, alias_of_id, latest_revision_id) FROM stdin;
1	0001	1	1	Root	root	t	f	/		f		\N	\N	f	1	\N	f	\N	\N	\N	\N	Root	\N	\N	45f1852e-f08b-45f7-a56f-4aa0f6b99119	1	\N	\N
3	00010001	2	0	Home	home	t	f	/home/		f		\N	\N	f	2	\N	f	\N	\N	\N	\N	Home	\N	\N	041399dc-cd54-44d0-ad07-976e95c39bc1	1	\N	\N
\.


--
-- TOC entry 3955 (class 0 OID 81983)
-- Dependencies: 252
-- Data for Name: home_homepage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.home_homepage (page_ptr_id) FROM stdin;
3
\.


--
-- TOC entry 3958 (class 0 OID 82003)
-- Dependencies: 255
-- Data for Name: taggit_tag; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.taggit_tag (id, name, slug) FROM stdin;
\.


--
-- TOC entry 3960 (class 0 OID 82013)
-- Dependencies: 257
-- Data for Name: taggit_taggeditem; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.taggit_taggeditem (id, object_id, content_type_id, tag_id) FROM stdin;
\.


--
-- TOC entry 3962 (class 0 OID 82037)
-- Dependencies: 259
-- Data for Name: wagtailadmin_admin; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailadmin_admin (id) FROM stdin;
\.


--
-- TOC entry 3946 (class 0 OID 81881)
-- Dependencies: 243
-- Data for Name: wagtailcore_collection; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_collection (id, path, depth, numchild, name) FROM stdin;
1	0001	1	0	Root
\.


--
-- TOC entry 3952 (class 0 OID 81951)
-- Dependencies: 249
-- Data for Name: wagtailcore_collectionviewrestriction; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_collectionviewrestriction (id, restriction_type, password, collection_id) FROM stdin;
\.


--
-- TOC entry 3954 (class 0 OID 81957)
-- Dependencies: 251
-- Data for Name: wagtailcore_collectionviewrestriction_groups; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_collectionviewrestriction_groups (id, collectionviewrestriction_id, group_id) FROM stdin;
\.


--
-- TOC entry 3982 (class 0 OID 82257)
-- Dependencies: 279
-- Data for Name: wagtailcore_comment; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_comment (id, text, contentpath, "position", created_at, updated_at, resolved_at, page_id, resolved_by_id, revision_created_id, user_id) FROM stdin;
\.


--
-- TOC entry 3984 (class 0 OID 82265)
-- Dependencies: 281
-- Data for Name: wagtailcore_commentreply; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_commentreply (id, text, created_at, updated_at, comment_id, user_id) FROM stdin;
\.


--
-- TOC entry 3964 (class 0 OID 82051)
-- Dependencies: 261
-- Data for Name: wagtailcore_task; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_task (id, name, active, content_type_id) FROM stdin;
1	Moderators approval	t	4
\.


--
-- TOC entry 3969 (class 0 OID 82068)
-- Dependencies: 266
-- Data for Name: wagtailcore_groupapprovaltask; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_groupapprovaltask (task_ptr_id) FROM stdin;
1
\.


--
-- TOC entry 3976 (class 0 OID 82099)
-- Dependencies: 273
-- Data for Name: wagtailcore_groupapprovaltask_groups; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_groupapprovaltask_groups (id, groupapprovaltask_id, group_id) FROM stdin;
1	1	1
\.


--
-- TOC entry 3948 (class 0 OID 81894)
-- Dependencies: 245
-- Data for Name: wagtailcore_groupcollectionpermission; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_groupcollectionpermission (id, collection_id, group_id, permission_id) FROM stdin;
1	1	1	98
2	1	2	98
3	1	1	99
4	1	2	99
5	1	1	101
6	1	2	101
7	1	1	102
8	1	2	102
9	1	1	103
10	1	2	103
11	1	1	105
12	1	2	105
\.


--
-- TOC entry 3938 (class 0 OID 81794)
-- Dependencies: 235
-- Data for Name: wagtailcore_grouppagepermission; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_grouppagepermission (id, group_id, page_id, permission_id) FROM stdin;
1	1	1	30
2	1	1	31
3	1	1	36
4	2	1	30
5	2	1	31
6	1	1	35
7	1	1	37
\.


--
-- TOC entry 3988 (class 0 OID 82329)
-- Dependencies: 285
-- Data for Name: wagtailcore_modellogentry; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_modellogentry (id, label, action, data, "timestamp", content_changed, deleted, object_id, content_type_id, user_id, uuid, revision_id) FROM stdin;
\.


--
-- TOC entry 3978 (class 0 OID 82207)
-- Dependencies: 275
-- Data for Name: wagtailcore_pagelogentry; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_pagelogentry (id, label, action, data, "timestamp", content_changed, deleted, content_type_id, page_id, revision_id, user_id, uuid) FROM stdin;
\.


--
-- TOC entry 3986 (class 0 OID 82273)
-- Dependencies: 283
-- Data for Name: wagtailcore_pagesubscription; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_pagesubscription (id, comment_notifications, page_id, user_id) FROM stdin;
\.


--
-- TOC entry 3942 (class 0 OID 81810)
-- Dependencies: 239
-- Data for Name: wagtailcore_pageviewrestriction; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_pageviewrestriction (id, password, page_id, restriction_type) FROM stdin;
\.


--
-- TOC entry 3950 (class 0 OID 81924)
-- Dependencies: 247
-- Data for Name: wagtailcore_pageviewrestriction_groups; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_pageviewrestriction_groups (id, pageviewrestriction_id, group_id) FROM stdin;
\.


--
-- TOC entry 3990 (class 0 OID 82442)
-- Dependencies: 287
-- Data for Name: wagtailcore_referenceindex; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_referenceindex (id, object_id, to_object_id, model_path, content_path, content_path_hash, base_content_type_id, content_type_id, to_content_type_id) FROM stdin;
\.


--
-- TOC entry 3944 (class 0 OID 81816)
-- Dependencies: 241
-- Data for Name: wagtailcore_site; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_site (id, hostname, port, is_default_site, root_page_id, site_name) FROM stdin;
2	localhost	80	t	3	
\.


--
-- TOC entry 3966 (class 0 OID 82057)
-- Dependencies: 263
-- Data for Name: wagtailcore_taskstate; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_taskstate (id, status, started_at, finished_at, content_type_id, revision_id, task_id, workflow_state_id, finished_by_id, comment) FROM stdin;
\.


--
-- TOC entry 3968 (class 0 OID 82063)
-- Dependencies: 265
-- Data for Name: wagtailcore_workflow; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_workflow (id, name, active) FROM stdin;
1	Moderators approval	t
\.


--
-- TOC entry 3991 (class 0 OID 82506)
-- Dependencies: 288
-- Data for Name: wagtailcore_workflowcontenttype; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_workflowcontenttype (content_type_id, workflow_id) FROM stdin;
\.


--
-- TOC entry 3972 (class 0 OID 82081)
-- Dependencies: 269
-- Data for Name: wagtailcore_workflowpage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_workflowpage (page_id, workflow_id) FROM stdin;
1	1
\.


--
-- TOC entry 3971 (class 0 OID 82074)
-- Dependencies: 268
-- Data for Name: wagtailcore_workflowstate; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_workflowstate (id, status, created_at, current_task_state_id, object_id, requested_by_id, workflow_id, content_type_id, base_content_type_id) FROM stdin;
\.


--
-- TOC entry 3974 (class 0 OID 82092)
-- Dependencies: 271
-- Data for Name: wagtailcore_workflowtask; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_workflowtask (id, sort_order, task_id, workflow_id) FROM stdin;
1	0	1	1
\.


--
-- TOC entry 3993 (class 0 OID 82539)
-- Dependencies: 290
-- Data for Name: wagtaildocs_document; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtaildocs_document (id, title, file, created_at, uploaded_by_user_id, collection_id, file_size, file_hash) FROM stdin;
\.


--
-- TOC entry 3995 (class 0 OID 82560)
-- Dependencies: 292
-- Data for Name: wagtaildocs_uploadeddocument; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtaildocs_uploadeddocument (id, file, uploaded_by_user_id) FROM stdin;
\.


--
-- TOC entry 3997 (class 0 OID 82572)
-- Dependencies: 294
-- Data for Name: wagtailembeds_embed; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailembeds_embed (id, url, max_width, type, html, title, author_name, provider_name, thumbnail_url, width, height, last_updated, hash, cache_until) FROM stdin;
\.


--
-- TOC entry 3999 (class 0 OID 82588)
-- Dependencies: 296
-- Data for Name: wagtailforms_formsubmission; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailforms_formsubmission (id, form_data, submit_time, page_id) FROM stdin;
\.


--
-- TOC entry 4001 (class 0 OID 82609)
-- Dependencies: 298
-- Data for Name: wagtailimages_image; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailimages_image (id, title, file, width, height, created_at, focal_point_x, focal_point_y, focal_point_width, focal_point_height, uploaded_by_user_id, file_size, collection_id, file_hash) FROM stdin;
\.


--
-- TOC entry 4003 (class 0 OID 82620)
-- Dependencies: 300
-- Data for Name: wagtailimages_rendition; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailimages_rendition (id, file, width, height, focal_point_key, filter_spec, image_id) FROM stdin;
\.


--
-- TOC entry 4005 (class 0 OID 82649)
-- Dependencies: 302
-- Data for Name: wagtailimages_uploadedimage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailimages_uploadedimage (id, file, uploaded_by_user_id) FROM stdin;
\.


--
-- TOC entry 4007 (class 0 OID 82663)
-- Dependencies: 304
-- Data for Name: wagtailredirects_redirect; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailredirects_redirect (id, old_path, is_permanent, redirect_link, redirect_page_id, site_id, automatically_created, created_at, redirect_page_route_path) FROM stdin;
\.


--
-- TOC entry 4009 (class 0 OID 82735)
-- Dependencies: 306
-- Data for Name: wagtailsearch_indexentry; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailsearch_indexentry (id, object_id, title_norm, content_type_id, autocomplete, title, body) FROM stdin;
\.


--
-- TOC entry 4011 (class 0 OID 82754)
-- Dependencies: 308
-- Data for Name: wagtailusers_userprofile; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailusers_userprofile (id, submitted_notifications, approved_notifications, rejected_notifications, user_id, preferred_language, current_time_zone, avatar, updated_comments_notifications, dismissibles, theme) FROM stdin;
\.


--
-- TOC entry 4017 (class 0 OID 0)
-- Dependencies: 220
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 2, true);


--
-- TOC entry 4018 (class 0 OID 0)
-- Dependencies: 222
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 18, true);


--
-- TOC entry 4019 (class 0 OID 0)
-- Dependencies: 218
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 175, true);


--
-- TOC entry 4020 (class 0 OID 0)
-- Dependencies: 226
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- TOC entry 4021 (class 0 OID 0)
-- Dependencies: 224
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 1, true);


--
-- TOC entry 4022 (class 0 OID 0)
-- Dependencies: 228
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- TOC entry 4023 (class 0 OID 0)
-- Dependencies: 230
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);


--
-- TOC entry 4024 (class 0 OID 0)
-- Dependencies: 216
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 43, true);


--
-- TOC entry 4025 (class 0 OID 0)
-- Dependencies: 214
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 203, true);


--
-- TOC entry 4026 (class 0 OID 0)
-- Dependencies: 254
-- Name: taggit_tag_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.taggit_tag_id_seq', 1, false);


--
-- TOC entry 4027 (class 0 OID 0)
-- Dependencies: 256
-- Name: taggit_taggeditem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.taggit_taggeditem_id_seq', 1, false);


--
-- TOC entry 4028 (class 0 OID 0)
-- Dependencies: 258
-- Name: wagtailadmin_admin_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailadmin_admin_id_seq', 1, false);


--
-- TOC entry 4029 (class 0 OID 0)
-- Dependencies: 242
-- Name: wagtailcore_collection_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_collection_id_seq', 1, true);


--
-- TOC entry 4030 (class 0 OID 0)
-- Dependencies: 250
-- Name: wagtailcore_collectionviewrestriction_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_collectionviewrestriction_groups_id_seq', 1, false);


--
-- TOC entry 4031 (class 0 OID 0)
-- Dependencies: 248
-- Name: wagtailcore_collectionviewrestriction_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_collectionviewrestriction_id_seq', 1, false);


--
-- TOC entry 4032 (class 0 OID 0)
-- Dependencies: 278
-- Name: wagtailcore_comment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_comment_id_seq', 1, false);


--
-- TOC entry 4033 (class 0 OID 0)
-- Dependencies: 280
-- Name: wagtailcore_commentreply_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_commentreply_id_seq', 1, false);


--
-- TOC entry 4034 (class 0 OID 0)
-- Dependencies: 272
-- Name: wagtailcore_groupapprovaltask_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_groupapprovaltask_groups_id_seq', 1, true);


--
-- TOC entry 4035 (class 0 OID 0)
-- Dependencies: 244
-- Name: wagtailcore_groupcollectionpermission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_groupcollectionpermission_id_seq', 12, true);


--
-- TOC entry 4036 (class 0 OID 0)
-- Dependencies: 234
-- Name: wagtailcore_grouppagepermission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_grouppagepermission_id_seq', 7, true);


--
-- TOC entry 4037 (class 0 OID 0)
-- Dependencies: 276
-- Name: wagtailcore_locale_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_locale_id_seq', 1, true);


--
-- TOC entry 4038 (class 0 OID 0)
-- Dependencies: 284
-- Name: wagtailcore_modellogentry_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_modellogentry_id_seq', 1, false);


--
-- TOC entry 4039 (class 0 OID 0)
-- Dependencies: 232
-- Name: wagtailcore_page_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_page_id_seq', 3, true);


--
-- TOC entry 4040 (class 0 OID 0)
-- Dependencies: 274
-- Name: wagtailcore_pagelogentry_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_pagelogentry_id_seq', 1, false);


--
-- TOC entry 4041 (class 0 OID 0)
-- Dependencies: 236
-- Name: wagtailcore_pagerevision_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_pagerevision_id_seq', 1, false);


--
-- TOC entry 4042 (class 0 OID 0)
-- Dependencies: 282
-- Name: wagtailcore_pagesubscription_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_pagesubscription_id_seq', 1, false);


--
-- TOC entry 4043 (class 0 OID 0)
-- Dependencies: 246
-- Name: wagtailcore_pageviewrestriction_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_pageviewrestriction_groups_id_seq', 1, false);


--
-- TOC entry 4044 (class 0 OID 0)
-- Dependencies: 238
-- Name: wagtailcore_pageviewrestriction_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_pageviewrestriction_id_seq', 1, false);


--
-- TOC entry 4045 (class 0 OID 0)
-- Dependencies: 286
-- Name: wagtailcore_referenceindex_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_referenceindex_id_seq', 1, false);


--
-- TOC entry 4046 (class 0 OID 0)
-- Dependencies: 240
-- Name: wagtailcore_site_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_site_id_seq', 2, true);


--
-- TOC entry 4047 (class 0 OID 0)
-- Dependencies: 260
-- Name: wagtailcore_task_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_task_id_seq', 1, true);


--
-- TOC entry 4048 (class 0 OID 0)
-- Dependencies: 262
-- Name: wagtailcore_taskstate_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_taskstate_id_seq', 1, false);


--
-- TOC entry 4049 (class 0 OID 0)
-- Dependencies: 264
-- Name: wagtailcore_workflow_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_workflow_id_seq', 1, true);


--
-- TOC entry 4050 (class 0 OID 0)
-- Dependencies: 267
-- Name: wagtailcore_workflowstate_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_workflowstate_id_seq', 1, false);


--
-- TOC entry 4051 (class 0 OID 0)
-- Dependencies: 270
-- Name: wagtailcore_workflowtask_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_workflowtask_id_seq', 1, true);


--
-- TOC entry 4052 (class 0 OID 0)
-- Dependencies: 289
-- Name: wagtaildocs_document_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtaildocs_document_id_seq', 1, false);


--
-- TOC entry 4053 (class 0 OID 0)
-- Dependencies: 291
-- Name: wagtaildocs_uploadeddocument_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtaildocs_uploadeddocument_id_seq', 1, false);


--
-- TOC entry 4054 (class 0 OID 0)
-- Dependencies: 293
-- Name: wagtailembeds_embed_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailembeds_embed_id_seq', 1, false);


--
-- TOC entry 4055 (class 0 OID 0)
-- Dependencies: 295
-- Name: wagtailforms_formsubmission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailforms_formsubmission_id_seq', 1, false);


--
-- TOC entry 4056 (class 0 OID 0)
-- Dependencies: 297
-- Name: wagtailimages_image_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailimages_image_id_seq', 1, false);


--
-- TOC entry 4057 (class 0 OID 0)
-- Dependencies: 299
-- Name: wagtailimages_rendition_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailimages_rendition_id_seq', 1, false);


--
-- TOC entry 4058 (class 0 OID 0)
-- Dependencies: 301
-- Name: wagtailimages_uploadedimage_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailimages_uploadedimage_id_seq', 1, false);


--
-- TOC entry 4059 (class 0 OID 0)
-- Dependencies: 303
-- Name: wagtailredirects_redirect_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailredirects_redirect_id_seq', 1, false);


--
-- TOC entry 4060 (class 0 OID 0)
-- Dependencies: 305
-- Name: wagtailsearch_indexentry_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailsearch_indexentry_id_seq', 1, false);


--
-- TOC entry 4061 (class 0 OID 0)
-- Dependencies: 307
-- Name: wagtailusers_userprofile_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailusers_userprofile_id_seq', 1, false);


-- Completed on 2024-04-30 00:19:07

--
-- PostgreSQL database dump complete
--

