#! /usr/bin/perl -w

#Scrape1.cgi - demonstrate screen-scraping in Perl
# Alex Greco (grecoa66)

use strict;
use CGI;
use WWW::Mechanize;     # This is the object that gets stuff
use HTML::TokeParser;   # This is the object that parses HTML
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
# create new web agent and get a page
my $agent = WWW::Mechanize->new();
$agent->get("http://willsaveworldforgold.com/");

# create new HTML parser and get the content from the web agent
my $stream = HTML::TokeParser->new(\$agent->{content});


# First, get the title:
# get the first "div" tag to setup the loop...
my $tag = $stream->get_tag("div");
while ($tag->[1]{id} and $tag->[1]{id} ne 'post-title') {
    $tag = $stream->get_tag("div");
}

# get the text of that tag:
my $comic_title = $stream->get_trimmed_text("/div");


# advance to the div with the cartoon:
while ($tag->[1]{id} and $tag->[1]{id} ne 'comic-1') {
    $tag = $stream->get_tag("div");
}

# get the cartoon:
my $toon = $stream->get_tag("img");

# get the attributes from the "img" tag:
my $source = $toon->[1]{'src'};
my $popup = $toon->[1]{'title'};
my $caption = $toon->[1]{'alt'};


# Generate a bunch of output:
my $cgi = new CGI;

print $cgi->header(-type=>'text/html'),
      $cgi->start_html('Greco Comics');

print $cgi->h1("$comic_title"), "\n";

print $cgi->p($caption), "\n";

print $cgi->img({src=>$source, alt=>$caption}), "\n\n";

print "\n\n\n";


# now do "StarSlip" (note: same objects re-used, no "new()" )
$agent->get("http://www.starslip.chainsawsuit.com");
$stream = HTML::TokeParser->new(\$agent->{content});


# Advance to the "div" tag we want:
 $tag = $stream->get_tag("div");
while (! $tag->[1]{id} ||
       ($tag->[1]{id} and $tag->[1]{id} ne 'comic')){
	$tag = $stream->get_tag("div");
}

# advance to the a:
 $toon = $stream->get_tag("a");

# advance to the image:
 $toon = $stream->get_tag("img");

# get the attribute from the tag:
 $source = $toon->[1]{'src'};

# add this to the CGI output
print $cgi->img({src=>$source, alt=>'star slip'}), "\n\n";

# now do "StarSlip" (note: same objects re-used, no "new()" )
 $agent->get("http://www.nedroid.com/");
 $stream = HTML::TokeParser->new(\$agent->{content});


 # Advance to the "div" tag we want:
    $tag = $stream->get_tag("div");
 while (! $tag->[1]{id} ||
         ($tag->[1]{id} and $tag->[1]{id} ne 'comic')){
            $tag = $stream->get_tag("div");
         }

         # advance to the image:
         $toon = $stream->get_tag("img");

         # get the attribute from the tag:
         $source = $toon->[1]{'src'};
	
	 # get the title:
 	 my $title = $toon->[1]{'title'};
         # add this to the CGI output
	 print $cgi->p($title), "\n\n"; 
         print $cgi->img({src=>$source, alt=>'back comic'}), "\n\n";

# ALL DONE!
print $cgi->end_html, "\n";
