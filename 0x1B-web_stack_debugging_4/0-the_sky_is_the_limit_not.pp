# puppet manifest to change number of limits request

exec { 'change number of limits for ULIMIT variable':
  provider => 'shell',
  command  => 'sudo sed -i "s/15/5000/" /etc/default/nginx && sudo service nginx restart',
}
