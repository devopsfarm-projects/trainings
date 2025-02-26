
# Grant 'create', 'read' , 'update', and ‘list’ permission
# to paths prefixed by 'secret/*'
path "jenkins/*" {
  capabilities = [ "create", "read", "update", "list" ]
}
