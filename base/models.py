# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AnysiteAccessActiondom(models.Model):
    target = models.CharField(max_length=100)
    principal_class = models.CharField(max_length=100)
    principal = models.IntegerField()
    authority = models.IntegerField()
    policy = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'anysite_access_actiondom'


class AnysiteAccessActions(models.Model):
    target = models.CharField(max_length=100)
    principal_class = models.CharField(max_length=100)
    principal = models.IntegerField()
    authority = models.IntegerField()
    policy = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'anysite_access_actions'


class AnysiteAccessCategory(models.Model):
    target = models.CharField(max_length=100)
    principal_class = models.CharField(max_length=100)
    principal = models.IntegerField()
    authority = models.IntegerField()
    policy = models.IntegerField()
    context_key = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'anysite_access_category'


class AnysiteAccessContext(models.Model):
    target = models.CharField(max_length=100)
    principal_class = models.CharField(max_length=100)
    principal = models.IntegerField()
    authority = models.IntegerField()
    policy = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'anysite_access_context'


class AnysiteAccessElements(models.Model):
    target = models.CharField(max_length=100)
    principal_class = models.CharField(max_length=100)
    principal = models.IntegerField()
    authority = models.IntegerField()
    policy = models.IntegerField()
    context_key = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'anysite_access_elements'


class AnysiteAccessMediaSource(models.Model):
    target = models.CharField(max_length=100)
    principal_class = models.CharField(max_length=100)
    principal = models.IntegerField()
    authority = models.IntegerField()
    policy = models.IntegerField()
    context_key = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'anysite_access_media_source'


class AnysiteAccessMenus(models.Model):
    target = models.CharField(max_length=100)
    principal_class = models.CharField(max_length=100)
    principal = models.IntegerField()
    authority = models.IntegerField()
    policy = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'anysite_access_menus'


class AnysiteAccessNamespace(models.Model):
    target = models.CharField(max_length=100)
    principal_class = models.CharField(max_length=100)
    principal = models.IntegerField()
    authority = models.IntegerField()
    policy = models.IntegerField()
    context_key = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'anysite_access_namespace'


class AnysiteAccessPermissions(models.Model):
    template = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'anysite_access_permissions'


class AnysiteAccessPolicies(models.Model):
    name = models.CharField(unique=True, max_length=255)
    description = models.TextField(blank=True, null=True)
    parent = models.IntegerField()
    template = models.IntegerField()
    class_field = models.CharField(db_column='class', max_length=255)  # Field renamed because it was a Python reserved word.
    data = models.TextField(blank=True, null=True)
    lexicon = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'anysite_access_policies'


class AnysiteAccessPolicyTemplateGroups(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'anysite_access_policy_template_groups'


class AnysiteAccessPolicyTemplates(models.Model):
    template_group = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    lexicon = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'anysite_access_policy_templates'


class AnysiteAccessResourceGroups(models.Model):
    target = models.CharField(max_length=100)
    principal_class = models.CharField(max_length=100)
    principal = models.IntegerField()
    authority = models.IntegerField()
    policy = models.IntegerField()
    context_key = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'anysite_access_resource_groups'


class AnysiteAccessResources(models.Model):
    target = models.CharField(max_length=100)
    principal_class = models.CharField(max_length=100)
    principal = models.IntegerField()
    authority = models.IntegerField()
    policy = models.IntegerField()
    context_key = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'anysite_access_resources'


class AnysiteAccessTemplatevars(models.Model):
    target = models.CharField(max_length=100)
    principal_class = models.CharField(max_length=100)
    principal = models.IntegerField()
    authority = models.IntegerField()
    policy = models.IntegerField()
    context_key = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'anysite_access_templatevars'


class AnysiteActiondom(models.Model):
    set = models.IntegerField()
    action = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    xtype = models.CharField(max_length=100)
    container = models.CharField(max_length=255)
    rule = models.CharField(max_length=100)
    value = models.TextField()
    constraint = models.CharField(max_length=255)
    constraint_field = models.CharField(max_length=100)
    constraint_class = models.CharField(max_length=100)
    active = models.IntegerField()
    for_parent = models.IntegerField()
    rank = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'anysite_actiondom'


class AnysiteActions(models.Model):
    namespace = models.CharField(max_length=100)
    controller = models.CharField(max_length=255)
    haslayout = models.IntegerField()
    lang_topics = models.TextField()
    assets = models.TextField()
    help_url = models.TextField()

    class Meta:
        managed = False
        db_table = 'anysite_actions'


class AnysiteActionsFields(models.Model):
    action = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    tab = models.CharField(max_length=255)
    form = models.CharField(max_length=255)
    other = models.CharField(max_length=255)
    rank = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'anysite_actions_fields'


class AnysiteActiveUsers(models.Model):
    internalkey = models.IntegerField(db_column='internalKey', primary_key=True)  # Field name made lowercase.
    username = models.CharField(max_length=50)
    lasthit = models.IntegerField()
    id = models.IntegerField(blank=True, null=True)
    action = models.CharField(max_length=255)
    ip = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'anysite_active_users'


class AnysiteCategories(models.Model):
    parent = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=45)
    rank = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'anysite_categories'
        unique_together = (('parent', 'category'),)


class AnysiteCategoriesClosure(models.Model):
    ancestor = models.IntegerField(primary_key=True)
    descendant = models.IntegerField()
    depth = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'anysite_categories_closure'
        unique_together = (('ancestor', 'descendant'),)


class AnysiteClassMap(models.Model):
    class_field = models.CharField(db_column='class', unique=True, max_length=120)  # Field renamed because it was a Python reserved word.
    parent_class = models.CharField(max_length=120)
    name_field = models.CharField(max_length=255)
    path = models.TextField(blank=True, null=True)
    lexicon = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'anysite_class_map'


class AnysiteContentType(models.Model):
    name = models.CharField(unique=True, max_length=255)
    description = models.TextField(blank=True, null=True)
    mime_type = models.TextField(blank=True, null=True)
    file_extensions = models.TextField(blank=True, null=True)
    headers = models.TextField(blank=True, null=True)
    binary = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'anysite_content_type'


class AnysiteContext(models.Model):
    key = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    rank = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'anysite_context'


class AnysiteContextResource(models.Model):
    context_key = models.CharField(primary_key=True, max_length=255)
    resource = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'anysite_context_resource'
        unique_together = (('context_key', 'resource'),)


class AnysiteContextSetting(models.Model):
    context_key = models.CharField(primary_key=True, max_length=255)
    key = models.CharField(max_length=50)
    value = models.TextField(blank=True, null=True)
    xtype = models.CharField(max_length=75)
    namespace = models.CharField(max_length=40)
    area = models.CharField(max_length=255)
    editedon = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'anysite_context_setting'
        unique_together = (('context_key', 'key'),)


class AnysiteDashboard(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    hide_trees = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'anysite_dashboard'


class AnysiteDashboardWidget(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    namespace = models.CharField(max_length=255)
    lexicon = models.CharField(max_length=255)
    size = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'anysite_dashboard_widget'


class AnysiteDashboardWidgetPlacement(models.Model):
    dashboard = models.IntegerField(primary_key=True)
    widget = models.IntegerField()
    rank = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'anysite_dashboard_widget_placement'
        unique_together = (('dashboard', 'widget'),)


class AnysiteDistricts(models.Model):
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'anysite_districts'


class AnysiteDocumentGroups(models.Model):
    document_group = models.IntegerField()
    document = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'anysite_document_groups'


class AnysiteDocumentgroupNames(models.Model):
    name = models.CharField(unique=True, max_length=255)
    private_memgroup = models.IntegerField()
    private_webgroup = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'anysite_documentgroup_names'


class AnysiteElementPropertySets(models.Model):
    element = models.IntegerField(primary_key=True)
    element_class = models.CharField(max_length=100)
    property_set = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'anysite_element_property_sets'
        unique_together = (('element', 'element_class', 'property_set'),)


class AnysiteExtensionPackages(models.Model):
    namespace = models.CharField(max_length=40)
    name = models.CharField(max_length=100)
    path = models.TextField(blank=True, null=True)
    table_prefix = models.CharField(max_length=255)
    service_class = models.CharField(max_length=255)
    service_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'anysite_extension_packages'


class AnysiteFcProfiles(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    active = models.IntegerField()
    rank = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'anysite_fc_profiles'


class AnysiteFcProfilesUsergroups(models.Model):
    usergroup = models.IntegerField(primary_key=True)
    profile = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'anysite_fc_profiles_usergroups'
        unique_together = (('usergroup', 'profile'),)


class AnysiteFcSets(models.Model):
    profile = models.IntegerField()
    action = models.CharField(max_length=255)
    description = models.TextField()
    active = models.IntegerField()
    template = models.IntegerField()
    constraint = models.CharField(max_length=255)
    constraint_field = models.CharField(max_length=100)
    constraint_class = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'anysite_fc_sets'


class AnysiteHctype(models.Model):
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'anysite_hcType'


class AnysiteLexiconEntries(models.Model):
    name = models.CharField(max_length=255)
    value = models.TextField()
    topic = models.CharField(max_length=255)
    namespace = models.CharField(max_length=40)
    language = models.CharField(max_length=20)
    createdon = models.DateTimeField(blank=True, null=True)
    editedon = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'anysite_lexicon_entries'


class AnysiteManagerLog(models.Model):
    user = models.IntegerField()
    occurred = models.DateTimeField(blank=True, null=True)
    action = models.CharField(max_length=100)
    classkey = models.CharField(db_column='classKey', max_length=100)  # Field name made lowercase.
    item = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'anysite_manager_log'


class AnysiteMediaSources(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    class_key = models.CharField(max_length=100)
    properties = models.TextField(blank=True, null=True)
    is_stream = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'anysite_media_sources'


class AnysiteMediaSourcesContexts(models.Model):
    source = models.IntegerField(primary_key=True)
    context_key = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'anysite_media_sources_contexts'
        unique_together = (('source', 'context_key'),)


class AnysiteMediaSourcesElements(models.Model):
    source = models.IntegerField(primary_key=True)
    object_class = models.CharField(max_length=100)
    object = models.IntegerField()
    context_key = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'anysite_media_sources_elements'
        unique_together = (('source', 'object', 'object_class', 'context_key'),)


class AnysiteMemberGroups(models.Model):
    user_group = models.IntegerField()
    member = models.IntegerField()
    role = models.IntegerField()
    rank = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'anysite_member_groups'


class AnysiteMembergroupNames(models.Model):
    name = models.CharField(unique=True, max_length=255)
    description = models.TextField(blank=True, null=True)
    parent = models.IntegerField()
    rank = models.IntegerField()
    dashboard = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'anysite_membergroup_names'


class AnysiteMenus(models.Model):
    text = models.CharField(primary_key=True, max_length=255)
    parent = models.CharField(max_length=255)
    action = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    menuindex = models.IntegerField()
    params = models.TextField()
    handler = models.TextField()
    permissions = models.TextField()
    namespace = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'anysite_menus'


class AnysiteMetro(models.Model):
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'anysite_metro'


class AnysiteMigxConfigElements(models.Model):
    config_id = models.IntegerField()
    element_id = models.IntegerField()
    rank = models.IntegerField()
    createdby = models.IntegerField()
    createdon = models.DateTimeField()
    editedby = models.IntegerField()
    editedon = models.DateTimeField()
    deleted = models.IntegerField()
    deletedon = models.DateTimeField()
    deletedby = models.IntegerField()
    published = models.IntegerField()
    publishedon = models.DateTimeField()
    publishedby = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'anysite_migx_config_elements'


class AnysiteMigxConfigs(models.Model):
    name = models.CharField(max_length=100)
    formtabs = models.TextField()
    contextmenus = models.TextField()
    actionbuttons = models.TextField()
    columnbuttons = models.TextField()
    filters = models.TextField()
    extended = models.TextField()
    columns = models.TextField()
    createdby = models.IntegerField()
    createdon = models.DateTimeField(blank=True, null=True)
    editedby = models.IntegerField()
    editedon = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField()
    deletedon = models.DateTimeField(blank=True, null=True)
    deletedby = models.IntegerField()
    published = models.IntegerField()
    publishedon = models.DateTimeField(blank=True, null=True)
    publishedby = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'anysite_migx_configs'


class AnysiteMigxElements(models.Model):
    type = models.CharField(max_length=100)
    content = models.TextField()
    createdby = models.IntegerField()
    createdon = models.DateTimeField()
    editedby = models.IntegerField()
    editedon = models.DateTimeField()
    deleted = models.IntegerField()
    deletedon = models.DateTimeField()
    deletedby = models.IntegerField()
    published = models.IntegerField()
    publishedon = models.DateTimeField()
    publishedby = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'anysite_migx_elements'


class AnysiteMigxFormtabFields(models.Model):
    config_id = models.IntegerField()
    formtab_id = models.IntegerField()
    field = models.CharField(max_length=255)
    caption = models.CharField(max_length=255)
    description = models.TextField()
    pos = models.IntegerField()
    description_is_code = models.IntegerField()
    inputtv = models.CharField(db_column='inputTV', max_length=255)  # Field name made lowercase.
    inputtvtype = models.CharField(db_column='inputTVtype', max_length=255)  # Field name made lowercase.
    validation = models.TextField()
    configs = models.CharField(max_length=255)
    restrictive_condition = models.TextField()
    display = models.CharField(max_length=255)
    sourcefrom = models.CharField(db_column='sourceFrom', max_length=255)  # Field name made lowercase.
    sources = models.CharField(max_length=255)
    inputoptionvalues = models.TextField(db_column='inputOptionValues')  # Field name made lowercase.
    default = models.TextField()
    extended = models.TextField()

    class Meta:
        managed = False
        db_table = 'anysite_migx_formtab_fields'


class AnysiteMigxFormtabs(models.Model):
    config_id = models.IntegerField()
    caption = models.CharField(max_length=255)
    pos = models.IntegerField()
    print_before_tabs = models.IntegerField()
    extended = models.TextField()

    class Meta:
        managed = False
        db_table = 'anysite_migx_formtabs'


class AnysiteNamespaces(models.Model):
    name = models.CharField(primary_key=True, max_length=40)
    path = models.TextField(blank=True, null=True)
    assets_path = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'anysite_namespaces'


class AnysiteObjecttype(models.Model):
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'anysite_objectType'


class AnysiteObjectspecies(models.Model):
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'anysite_objectspecies'


class AnysitePropertySet(models.Model):
    name = models.CharField(unique=True, max_length=50)
    category = models.IntegerField()
    description = models.CharField(max_length=255)
    properties = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'anysite_property_set'


class AnysiteRegions(models.Model):
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'anysite_regions'


class AnysiteRegisterMessages(models.Model):
    topic = models.IntegerField(primary_key=True)
    id = models.CharField(max_length=255)
    created = models.DateTimeField()
    valid = models.DateTimeField()
    accessed = models.DateTimeField(blank=True, null=True)
    accesses = models.IntegerField()
    expires = models.IntegerField()
    payload = models.TextField()
    kill = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'anysite_register_messages'
        unique_together = (('topic', 'id'),)


class AnysiteRegisterQueues(models.Model):
    name = models.CharField(unique=True, max_length=255)
    options = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'anysite_register_queues'


class AnysiteRegisterTopics(models.Model):
    queue = models.IntegerField()
    name = models.CharField(max_length=255)
    created = models.DateTimeField()
    updated = models.DateTimeField(blank=True, null=True)
    options = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'anysite_register_topics'


class AnysiteSession(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    access = models.IntegerField()
    data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'anysite_session'


class AnysiteSiteContent(models.Model):
    type = models.CharField(max_length=20)
    contenttype = models.CharField(db_column='contentType', max_length=50)  # Field name made lowercase.
    pagetitle = models.CharField(max_length=255)
    longtitle = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    alias = models.CharField(max_length=255, blank=True, null=True)
    link_attributes = models.CharField(max_length=255)
    published = models.IntegerField()
    pub_date = models.IntegerField()
    unpub_date = models.IntegerField()
    parent = models.IntegerField()
    isfolder = models.IntegerField()
    introtext = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    richtext = models.IntegerField()
    template = models.IntegerField()
    menuindex = models.IntegerField()
    searchable = models.IntegerField()
    cacheable = models.IntegerField()
    createdby = models.IntegerField()
    createdon = models.IntegerField()
    editedby = models.IntegerField()
    editedon = models.IntegerField()
    deleted = models.IntegerField()
    deletedon = models.IntegerField()
    deletedby = models.IntegerField()
    publishedon = models.IntegerField()
    publishedby = models.IntegerField()
    menutitle = models.CharField(max_length=255)
    donthit = models.IntegerField()
    privateweb = models.IntegerField()
    privatemgr = models.IntegerField()
    content_dispo = models.IntegerField()
    hidemenu = models.IntegerField()
    class_key = models.CharField(max_length=100)
    context_key = models.CharField(max_length=100)
    content_type = models.IntegerField()
    uri = models.TextField(blank=True, null=True)
    uri_override = models.IntegerField()
    hide_children_in_tree = models.IntegerField()
    show_in_tree = models.IntegerField()
    properties = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'anysite_site_content'


class AnysiteSiteHtmlsnippets(models.Model):
    source = models.IntegerField()
    property_preprocess = models.IntegerField()
    name = models.CharField(unique=True, max_length=50)
    description = models.CharField(max_length=255)
    editor_type = models.IntegerField()
    category = models.IntegerField()
    cache_type = models.IntegerField()
    snippet = models.TextField(blank=True, null=True)
    locked = models.IntegerField()
    properties = models.TextField(blank=True, null=True)
    static = models.IntegerField()
    static_file = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'anysite_site_htmlsnippets'


class AnysiteSitePluginEvents(models.Model):
    pluginid = models.IntegerField(primary_key=True)
    event = models.CharField(max_length=255)
    priority = models.IntegerField()
    propertyset = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'anysite_site_plugin_events'
        unique_together = (('pluginid', 'event'),)


class AnysiteSitePlugins(models.Model):
    source = models.IntegerField()
    property_preprocess = models.IntegerField()
    name = models.CharField(unique=True, max_length=50)
    description = models.CharField(max_length=255)
    editor_type = models.IntegerField()
    category = models.IntegerField()
    cache_type = models.IntegerField()
    plugincode = models.TextField()
    locked = models.IntegerField()
    properties = models.TextField(blank=True, null=True)
    disabled = models.IntegerField()
    moduleguid = models.CharField(max_length=32)
    static = models.IntegerField()
    static_file = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'anysite_site_plugins'


class AnysiteSiteSnippets(models.Model):
    source = models.IntegerField()
    property_preprocess = models.IntegerField()
    name = models.CharField(unique=True, max_length=50)
    description = models.CharField(max_length=255)
    editor_type = models.IntegerField()
    category = models.IntegerField()
    cache_type = models.IntegerField()
    snippet = models.TextField(blank=True, null=True)
    locked = models.IntegerField()
    properties = models.TextField(blank=True, null=True)
    moduleguid = models.CharField(max_length=32)
    static = models.IntegerField()
    static_file = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'anysite_site_snippets'


class AnysiteSiteTemplates(models.Model):
    source = models.IntegerField()
    property_preprocess = models.IntegerField()
    templatename = models.CharField(unique=True, max_length=50)
    description = models.CharField(max_length=255)
    editor_type = models.IntegerField()
    category = models.IntegerField()
    icon = models.CharField(max_length=255)
    template_type = models.IntegerField()
    content = models.TextField()
    locked = models.IntegerField()
    properties = models.TextField(blank=True, null=True)
    static = models.IntegerField()
    static_file = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'anysite_site_templates'


class AnysiteSiteTmplvarAccess(models.Model):
    tmplvarid = models.IntegerField()
    documentgroup = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'anysite_site_tmplvar_access'


class AnysiteSiteTmplvarContentvalues(models.Model):
    tmplvarid = models.IntegerField()
    contentid = models.IntegerField()
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'anysite_site_tmplvar_contentvalues'


class AnysiteSiteTmplvarTemplates(models.Model):
    tmplvarid = models.IntegerField(primary_key=True)
    templateid = models.IntegerField()
    rank = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'anysite_site_tmplvar_templates'
        unique_together = (('tmplvarid', 'templateid'),)


class AnysiteSiteTmplvars(models.Model):
    source = models.IntegerField()
    property_preprocess = models.IntegerField()
    type = models.CharField(max_length=20)
    name = models.CharField(unique=True, max_length=50)
    caption = models.CharField(max_length=80)
    description = models.CharField(max_length=255)
    editor_type = models.IntegerField()
    category = models.IntegerField()
    locked = models.IntegerField()
    elements = models.TextField(blank=True, null=True)
    rank = models.IntegerField()
    display = models.CharField(max_length=20)
    default_text = models.TextField(blank=True, null=True)
    properties = models.TextField(blank=True, null=True)
    input_properties = models.TextField(blank=True, null=True)
    output_properties = models.TextField(blank=True, null=True)
    static = models.IntegerField()
    static_file = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'anysite_site_tmplvars'


class AnysiteSystemEventnames(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    service = models.IntegerField()
    groupname = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'anysite_system_eventnames'


class AnysiteSystemSettings(models.Model):
    key = models.CharField(primary_key=True, max_length=50)
    value = models.TextField()
    xtype = models.CharField(max_length=75)
    namespace = models.CharField(max_length=40)
    area = models.CharField(max_length=255)
    editedon = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'anysite_system_settings'


class AnysiteTicketsAuthorActions(models.Model):
    id = models.IntegerField(primary_key=True)
    action = models.CharField(max_length=50)
    owner = models.IntegerField()
    rating = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    multiplier = models.IntegerField(blank=True, null=True)
    ticket = models.IntegerField()
    section = models.IntegerField()
    createdby = models.IntegerField()
    createdon = models.DateTimeField()
    year = models.TextField(blank=True, null=True)  # This field type is a guess.
    month = models.IntegerField(blank=True, null=True)
    day = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'anysite_tickets_author_actions'
        unique_together = (('id', 'action', 'owner', 'createdby'),)


class AnysiteTicketsAuthors(models.Model):
    id = models.IntegerField(primary_key=True)
    rating = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    createdon = models.DateTimeField(blank=True, null=True)
    visitedon = models.DateTimeField(blank=True, null=True)
    tickets = models.IntegerField(blank=True, null=True)
    comments = models.IntegerField(blank=True, null=True)
    views = models.IntegerField(blank=True, null=True)
    votes_tickets = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    votes_comments = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    stars_tickets = models.IntegerField(blank=True, null=True)
    stars_comments = models.IntegerField(blank=True, null=True)
    votes_tickets_up = models.IntegerField(blank=True, null=True)
    votes_tickets_down = models.IntegerField(blank=True, null=True)
    votes_comments_up = models.IntegerField(blank=True, null=True)
    votes_comments_down = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'anysite_tickets_authors'


class AnysiteTicketsComments(models.Model):
    thread = models.IntegerField()
    parent = models.IntegerField()
    text = models.TextField()
    raw = models.TextField()
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    ip = models.CharField(max_length=16)
    rating = models.SmallIntegerField(blank=True, null=True)
    rating_plus = models.SmallIntegerField(blank=True, null=True)
    rating_minus = models.SmallIntegerField(blank=True, null=True)
    createdon = models.DateTimeField(blank=True, null=True)
    createdby = models.IntegerField()
    editedon = models.DateTimeField(blank=True, null=True)
    editedby = models.IntegerField()
    published = models.IntegerField()
    deleted = models.IntegerField()
    deletedon = models.DateTimeField(blank=True, null=True)
    deletedby = models.IntegerField()
    properties = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'anysite_tickets_comments'


class AnysiteTicketsFiles(models.Model):
    parent = models.IntegerField()
    class_field = models.CharField(db_column='class', max_length=100, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    source = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    path = models.CharField(max_length=255)
    file = models.CharField(max_length=255)
    type = models.CharField(max_length=50, blank=True, null=True)
    size = models.IntegerField()
    createdon = models.DateTimeField(blank=True, null=True)
    createdby = models.IntegerField()
    url = models.CharField(max_length=255)
    thumb = models.CharField(max_length=255)
    thumbs = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    properties = models.TextField(blank=True, null=True)
    hash = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'anysite_tickets_files'


class AnysiteTicketsMailQueues(models.Model):
    timestamp = models.DateTimeField()
    uid = models.IntegerField()
    subject = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'anysite_tickets_mail_queues'


class AnysiteTicketsStars(models.Model):
    id = models.IntegerField(primary_key=True)
    class_field = models.CharField(db_column='class', max_length=100)  # Field renamed because it was a Python reserved word.
    owner = models.IntegerField()
    createdon = models.DateTimeField(blank=True, null=True)
    createdby = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'anysite_tickets_stars'
        unique_together = (('id', 'createdby', 'class_field'),)


class AnysiteTicketsThreads(models.Model):
    resource = models.IntegerField()
    name = models.CharField(unique=True, max_length=255)
    subscribers = models.TextField()
    createdon = models.DateTimeField(blank=True, null=True)
    createdby = models.IntegerField()
    closed = models.IntegerField()
    deleted = models.IntegerField()
    deletedon = models.DateTimeField(blank=True, null=True)
    deletedby = models.IntegerField()
    comment_last = models.IntegerField()
    comment_time = models.DateTimeField(blank=True, null=True)
    comments = models.IntegerField(blank=True, null=True)
    properties = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'anysite_tickets_threads'


class AnysiteTicketsViews(models.Model):
    parent = models.IntegerField(primary_key=True)
    uid = models.IntegerField()
    guest_key = models.CharField(max_length=32)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'anysite_tickets_views'
        unique_together = (('parent', 'uid', 'guest_key'),)


class AnysiteTicketsVotes(models.Model):
    id = models.IntegerField(primary_key=True)
    class_field = models.CharField(db_column='class', max_length=100)  # Field renamed because it was a Python reserved word.
    owner = models.IntegerField()
    value = models.IntegerField()
    createdon = models.DateTimeField(blank=True, null=True)
    createdby = models.IntegerField()
    ip = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'anysite_tickets_votes'
        unique_together = (('id', 'createdby', 'class_field'),)


class AnysiteTransportPackages(models.Model):
    signature = models.CharField(primary_key=True, max_length=255)
    created = models.DateTimeField()
    updated = models.DateTimeField(blank=True, null=True)
    installed = models.DateTimeField(blank=True, null=True)
    state = models.IntegerField()
    workspace = models.IntegerField()
    provider = models.IntegerField()
    disabled = models.IntegerField()
    source = models.TextField(blank=True, null=True)
    manifest = models.TextField(blank=True, null=True)
    attributes = models.TextField(blank=True, null=True)
    package_name = models.CharField(max_length=255)
    metadata = models.TextField(blank=True, null=True)
    version_major = models.SmallIntegerField()
    version_minor = models.SmallIntegerField()
    version_patch = models.SmallIntegerField()
    release = models.CharField(max_length=100)
    release_index = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'anysite_transport_packages'


class AnysiteTransportProviders(models.Model):
    name = models.CharField(unique=True, max_length=255)
    description = models.TextField(blank=True, null=True)
    service_url = models.TextField(blank=True, null=True)
    username = models.CharField(max_length=255)
    api_key = models.CharField(max_length=255)
    created = models.DateTimeField()
    updated = models.DateTimeField(blank=True, null=True)
    active = models.IntegerField()
    priority = models.IntegerField()
    properties = models.TextField()

    class Meta:
        managed = False
        db_table = 'anysite_transport_providers'


class AnysiteUserAttributes(models.Model):
    internalkey = models.IntegerField(db_column='internalKey', unique=True)  # Field name made lowercase.
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    mobilephone = models.CharField(max_length=100)
    blocked = models.IntegerField()
    blockeduntil = models.IntegerField()
    blockedafter = models.IntegerField()
    logincount = models.IntegerField()
    lastlogin = models.IntegerField()
    thislogin = models.IntegerField()
    failedlogincount = models.IntegerField()
    sessionid = models.CharField(max_length=100)
    dob = models.IntegerField()
    gender = models.IntegerField()
    address = models.TextField()
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=25)
    zip = models.CharField(max_length=25)
    fax = models.CharField(max_length=100)
    photo = models.CharField(max_length=255)
    comment = models.TextField()
    website = models.CharField(max_length=255)
    extended = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'anysite_user_attributes'


class AnysiteUserGroupRoles(models.Model):
    name = models.CharField(unique=True, max_length=255)
    description = models.TextField(blank=True, null=True)
    authority = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'anysite_user_group_roles'


class AnysiteUserGroupSettings(models.Model):
    group = models.IntegerField(primary_key=True)
    key = models.CharField(max_length=50)
    value = models.TextField(blank=True, null=True)
    xtype = models.CharField(max_length=75)
    namespace = models.CharField(max_length=40)
    area = models.CharField(max_length=255)
    editedon = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'anysite_user_group_settings'
        unique_together = (('group', 'key'),)


class AnysiteUserMessages(models.Model):
    type = models.CharField(max_length=15)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sender = models.IntegerField()
    recipient = models.IntegerField()
    private = models.IntegerField()
    date_sent = models.DateTimeField()
    read = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'anysite_user_messages'


class AnysiteUserSettings(models.Model):
    user = models.IntegerField(primary_key=True)
    key = models.CharField(max_length=50)
    value = models.TextField(blank=True, null=True)
    xtype = models.CharField(max_length=75)
    namespace = models.CharField(max_length=40)
    area = models.CharField(max_length=255)
    editedon = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'anysite_user_settings'
        unique_together = (('user', 'key'),)


class AnysiteUsers(models.Model):
    username = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)
    cachepwd = models.CharField(max_length=100)
    class_key = models.CharField(max_length=100)
    active = models.IntegerField()
    remote_key = models.CharField(max_length=255, blank=True, null=True)
    remote_data = models.TextField(blank=True, null=True)
    hash_class = models.CharField(max_length=100)
    salt = models.CharField(max_length=100)
    primary_group = models.IntegerField()
    session_stale = models.TextField(blank=True, null=True)
    sudo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'anysite_users'


class AnysiteWorkspaces(models.Model):
    name = models.CharField(max_length=255)
    path = models.CharField(unique=True, max_length=255)
    created = models.DateTimeField()
    active = models.IntegerField()
    attributes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'anysite_workspaces'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
