from AccessControl import allow_class, ModuleSecurityInfo, ClassSecurityInfo

ModuleSecurityInfo("collective.taskqueue.taskqueue").declarePublic("add")
