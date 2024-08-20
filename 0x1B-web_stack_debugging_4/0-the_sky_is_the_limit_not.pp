# Puppet manuscript to increase nginx traffic limit


exec { 'nginx-fix':
  command => 'sed -i "s/15/5000" /etc/default/nginx',
  path    => '/usr/local/bin:/usr/bin:/bin',
}

exec { 'restart-nginx':
  command     => '/usr/sbin/service nginx restart',
  refreshonly => true,
  subscribe   => Service['nginx'],
}
