## First Jekyll Page

### 1. Jekyll 템플릿 생성

```cmd
C:\Workspace\FIRST_JEKYLL>jekyll new .
Running bundle install in C:/Workspace/FIRST_JEKYLL...
  Bundler: Fetching gem metadata from https://rubygems.org/............
  Bundler: Fetching gem metadata from https://rubygems.org/..
  Bundler: Resolving dependencies...
  
  ...
  
  Bundler: Fetching wdm 0.1.1
  Bundler: Installing wdm 0.1.1 with native extensions
  Bundler: Bundle complete! 6 Gemfile dependencies, 34 gems now installed.
  Bundler: Use `bundle info [gemname]` to see where a bundled gem is installed.
New jekyll site installed in C:/Workspace/FIRST_JEKYLL.
```



이후 `jekyll serve` 명령어를 통해 Jekyll 서버를 실행시키면 Jekyll 템플릿에서 `Welcome to Jekyll`이 반겨준다.



#### 생성된 템플릿 구조

```
C:\WORKSPACE\FIRST_JEKYLL
│  .gitignore
│  404.html
│  about.markdown
│  Gemfile
│  Gemfile.lock
│  index.markdown
│  _config.yml
│
├─ .jekyll-cache
│
├─ _posts
│      2019-11-22-welcome-to-jekyll.markdown
│
└─ _site
    │  404.html
    │  feed.xml
    │  index.html
    │
    ├─ about
    │      index.html
    │
    ├─ assets
    │      main.css
    │      main.css.map
    │      minima-social-icons.svg
    │
    └─ jekyll
        └─update
            └─2019
                └─11
                    └─22
                            welcome-to-jekyll.html
```



