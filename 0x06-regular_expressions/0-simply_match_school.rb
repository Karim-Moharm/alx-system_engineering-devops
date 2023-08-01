#!/usr/bin/env ruby
# regular expression for matching the word School
puts ARGV[0].scan(/S[a-z]*/).join
