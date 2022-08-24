To build locally, follow the instructions at
	
 	https://github.com/pages-themes/minimal

in particular

```
gem install bundler
bundle install
```

I also needed to add

```
gem "github-pages", group: :jekyll_plugins
```

to the Gem file and run

```
bundle add webrick
```
