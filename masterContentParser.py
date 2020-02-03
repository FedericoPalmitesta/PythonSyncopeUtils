import re


def parse_string(string):
    string = string.replace("<", '')
    string = string.replace(">", '')
    string = string.replace("=", '')
    string = string.replace("/", '')
    string = re.sub(r'\".?\"', '', string)
    return re.sub(r'\".+?\"', '', string)


dictionary = {'IDP_ID': 'idp_id', 'PERFORMUPDATE': 'performUpdate', 'DERSCHEMA': 'DerSchema',
                  'PULLPOLICY': 'PullPolicy', 'PARENT_ID': 'parent_id', 'UPDATETRACELEVEL': 'updateTraceLevel',
                  'UNMATCHINGRULE': 'unmatchingRule', 'ANYTYPE_ANYTYPECLASS': 'AnyType_AnyTypeClass',
                  'CONNINSTANCE_CAPABILITIES': 'ConnInstance_capabilities', 'GROUP_ID': 'group_id',
                  'SYNCOPEROLE_REALM': 'SyncopeRole_Realm', 'PLAINSCHEMA': 'PlainSchema', 'RESOURCE_ID': 'resource_id',
                  'PROVISIONINGTRACELEVEL': 'provisioningTraceLevel', 'DYNREALMMEMBERSHIP': 'DynRealmMembership',
                  'PROVISION_ID': 'provision_id', 'PURPOSE': 'purpose', 'CONNREQUESTTIMEOUT': 'connRequestTimeout',
                  'DTYPE': 'dType', 'CREATIONDATE': 'creationDate', 'CREATOR': 'creator', 'CAPABILITY': 'capability',
                  'SYNCSTATUS': 'syncStatus', 'PULLTASKACTION': 'PullTaskAction', 'JSONCONF': 'jsonConf',
                  'SYNCOPEROLE_ENTITLEMENTS': 'SyncopeRole_Entitlements', 'ROLE_ID': 'role_id', 'TASK_ID': 'task_id',
                  'SAML2IDPITEM': 'Saml2IdpItem', 'IGNORECASEMATCH': 'ignoreCaseMatch',
                  'PERFORMCREATE': 'performCreate', 'UNIQUECONSTRAINT': 'uniqueConstraint', 'OWNER_ID': 'owner_id',
                  'LONGVALUE': 'longValue', 'STRINGVALUE': 'stringValue', 'ATTRIBUTE_ID': 'attribute_id',
                  'CPLAINATTR': 'CPlainAttr', 'LASTCHANGEDATE': 'lastChangeDate', 'MAPPINGITEM': 'MappingItem',
                  'EXTATTRNAME': 'extAttrName', 'VERSION': 'Version', 'MULTIVALUE': 'multivalue',
                  'ENTITLEMENT': 'entitlement', 'DISPLAYNAME': 'displayName', 'DESCRIPTION': 'description',
                  'LOCATION': 'location', 'TYPE': 'type', 'NAME': 'name', 'APPLICATION': 'Application',
                  'REALM_ID': 'realm_id', 'ACTIVE': 'active', 'RECIPIENTATTRNAME': 'recipientAttrName',
                  'CREATEUNMATCHING': 'createUnmatching', 'EXTERNALRESOURCEPROPACTION': 'ExternalResourcePropAction',
                  'METADATA': 'metadata', 'BUNDLENAME': 'bundleName', 'PERFORMDELETE': 'performDelete',
                  'SYNCOPEGROUP': 'SyncopeGroup', 'ANYTYPECLASS': 'AnyTypeClass', 'MATCHINGRULE': 'matchingRule',
                  'TYPEEXTENSION_ANYTYPECLASS': 'TypeExtension_AnyTypeClass', 'ANYTYPE': 'AnyType',
                  'SYNCOPECONF': 'SyncopeConf', 'REALM': 'Realm', 'BOOLEANVALUE': 'booleanValue',
                  'CONNOBJECTKEY': 'connObjectKey', 'PASSWORD': 'password', 'REALMACTION': 'RealmAction',
                  'PULLPOLICY_ID': 'pullPolicy_id', 'CONNINSTANCE': 'ConnInstance', 'EXPRESSION': 'expression',
                  'ENTITYID': 'entityId', 'SPEC': 'spec', 'JOBDELEGATE_ID': 'jobDelegate_id', 'REPORT_ID': 'report_id',
                  'DELETETRACELEVEL': 'deleteTraceLevel', 'SYNCOPESCHEMA': 'SyncopeSchema', 'PULLMODE': 'pullMode',
                  'PULLCORRELATIONRULEENTITY': 'PullCorrelationRuleEntity', 'LOGLEVEL': 'logLevel',
                  'INTATTRNAME': 'intAttrName', 'SCHEMA_ID': 'schema_id', 'KIND': 'kind', 'PRIVILEGE': 'Privilege',
                  'LOGNAME': 'logName', 'SYNCOPEROLE': 'SyncopeRole', 'SYNCOPEDOMAIN': 'SyncopeDomain',
                  'ADMINREALM_ID': 'adminRealm_id', 'CONNECTORNAME': 'connectorName', 'SAML2IDP': 'Saml2Idp',
                  'ANYTYPECLASS_ID': 'anyTypeClass_id', 'PROVISION': 'Provision', 'IMPLEMENTATION': 'Implementation',
                  'SECURITYQUESTION': 'SecurityQuestion', 'CONNECTOR_ID': 'connector_id', 'DYNREALM_ID': 'dynRealm_id',
                  'TYPEEXTENSION': 'TypeExtension', 'GPLAINATTRVALUE': 'GPlainAttrValue', 'GPLAINATTR': 'GPlainAttr',
                  'DESTINATIONREALM_ID': 'destinationRealm_id', 'SYNCOPELOGGER': 'SyncopeLogger',
                  'READONLY': 'readonly', 'CONFLICTRESOLUTIONACTION': 'conflictResolutionAction',
                  'SELFREGUNMATCHING': 'selfRegUnmatching', 'CREATETRACELEVEL': 'createTraceLevel',
                  'ENFORCEMANDATORYCONDITION': 'enforceMandatoryCondition', 'CONNINSTANCE_ID': 'connInstance_id',
                  'EXTERNALRESOURCE': 'ExternalResource', 'MANDATORYCONDITION': 'mandatoryCondition',
                  'RANDOMPWDIFNOTPROVIDED': 'randomPwdIfNotProvided', 'ANYTYPE_ID': 'anyType_id', 'MAPPING': 'Mapping',
                  'USEDEFLATEENCODING': 'useDeflateEncoding', 'ENUMERATIONVALUES': 'enumerationValues', 'TASK': 'Task',
                  'ADMINPWD': 'adminPwd', 'PRIVILEGE_ID': 'privilege_id', 'VALIDATOR_ID': 'validator_id',
                  'SUPPORTUNSOLICITED': 'supportUnsolicited', 'OBJECTCLASS': 'objectClass', 'REPORT': 'Report',
                  'UPDATEMATCHING': 'updateMatching', 'LOGTYPE': 'logType', 'BINDINGTYPE': 'bindingType',
                  'ANYLAYOUT': 'anyLayout', 'ADMINCIPHERALGORITHM': 'adminCipherAlgorithm', 'SENDER': 'sender',
                  'REMEDIATION': 'remediation', 'CPLAINATTRVALUE': 'CPlainAttrValue', 'ENGINE': 'engine',
                  'IMPLEMENTATION_ID': 'implementation_id', 'ID': 'id', 'FIQL': 'fiql', 'BODY': 'body',
                  'PROVISION_ANYTYPECLASS': 'Provision_anyTypeClass', 'CAPABILITYOVERRIDE': 'capabilityOverride',
                  'CONTENT': 'content', 'TYPEEXTENSION_ID': 'typeExtension_id', 'MIMETYPE': 'mimeType',
                  'SYNCOPEROLE_PRIVILEGE': 'SyncopeRole_Privilege', 'OVERRIDECAPABILITIES': 'overrideCapabilities',
                  'CONVERSIONPATTERN': 'conversionPattern', 'PROPJEXL': 'propjexl', 'PULLJEXL': 'pulljexl',
                  'EXTERNALRESOURCE_CAPOVERRIDE': 'ExternalResource_capOverride', 'APPLICATION_ID': 'application_id',
                  'LASTMODIFIER': 'lastModifier', 'ENUMERATIONKEYS': 'enumerationKeys', 'HTMLTEMPLATE': 'htmlTemplate',
                  'ANYTEMPLATEREALM': 'anyTemplateRealm', 'TEMPLATE': 'template', 'ITEM_ID': 'item_id',
                  'MAPPINGITEMTRANSFORMER': 'MappingItemTransformer', 'DYNREALM': 'DynRealm', 'EVENT': 'event',
                  'SYNCOPEGROUP_ANYTYPECLASS': 'SyncopeGroup_anyTypeClass', 'TEXTTEMPLATE': 'textTemplate',
                  'SYNCOPEGROUP_EXTERNALRESOURCE': 'SyncopeGroup_externalResource' , 'MAILTEMPLATE': 'MailTemplate',
                  'NOTIFICATION_ID': 'notification_id', 'NOTIFICATION_EVENTS': 'Notification_events',
                  'NOTIFICATION_STATICRECIPIENTS': 'Notification_staticRecipients', 'NOTIFICATION': 'Notification',
                  'STATICRECIPIENTS': 'staticRecipients', 'TEMPLATE_ID': 'template_id', 'SUBJECT': 'subject',
                  'SELFASRECIPIENT': 'selfAsRecipient', 'TRACELEVEL': 'traceLevel', 'MAPPING_ID': 'mapping_id',
                  'REPORTLETCONFINSTANCE': 'ReportletConfInstance', 'SERIALIZEDINSTANCE': 'serializedInstance',
                  'REPORTTEMPLATE': 'ReportTemplate', 'REPORTREPORTLET': 'ReportReportlet', 'FOTEMPLATE': 'foTemplate',
                  'SYNCOPEROLE_DYNREALM': 'SyncopeRole_dynRealm', 'DYNAMICREALM_ID': 'dynamicRealm_id'}

old_file = input("Provide the path of the source MasterContent (/path/MasterContent.xml): ")
new_file = input("Provide the path of the destination file (/path/file.xml): ")
with open(old_file) as oldfile, open(new_file, 'w') as newfile:
    for line in oldfile:
        for word in parse_string(line).split():
            line = line.replace(word, dictionary.get(word, word), 1)
        newfile.write(line)

print("Parsing succeeded")
