local:
	 clear; bundle exec jekyll serve

update:
	 clear; sudo bundle update
update_ruby:
	clear; LDFLAGS="" rbenv install 3.4.1
	