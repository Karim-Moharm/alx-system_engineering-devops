# fixing the extension for php file from phpp to php
exec { 'fixing extension of php file':
  command => 'sed -i "s/class-wp-locale.phpp/class-wp-locale.php/g" /var/www/html/wp-settings.php'
  path    => ['/usr/bin/', '/usr/sbin/']
}
