#!/usr/bin/ruby
# Print statistics from database

Dir.chdir File.dirname(__FILE__)

tables = Hash['Servers' => 'servers', 'Users' => 'users', 'Messages' => 'chat_log']
tables.each { |label, table|
        puts "#{label}: " + `sqlite3 cathy.db "select count(*) from #{table};"`
}
