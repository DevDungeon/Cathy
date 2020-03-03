#!/usr/bin/ruby
# Print statistics from database

Dir.chdir File.dirname(__FILE__)

first_msg_date = `sqlite3 cathy.db "select time from chat_log order by time asc limit 1;"`
puts "Since #{first_msg_date}"

tables = Hash['Servers' => 'servers', 'Users' => 'users', 'Messages' => 'chat_log']
tables.each { |label, table|
        puts "#{label}: " + `sqlite3 cathy.db "select count(*) from #{table};"`
}
