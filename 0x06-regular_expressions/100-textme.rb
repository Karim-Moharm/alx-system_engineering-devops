#!/usr/bin/env ruby
puts ARGV[0].scan(/\[from:(\+*\w*)\]\s\[to:(\+\d*\W*)\]\s\[flags:(.*?)\]/).join
