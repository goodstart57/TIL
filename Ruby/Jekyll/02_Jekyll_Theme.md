# Jekyll > Theme

`지킬 테마`를 이용하여 `깃블로그` 간편하게 꾸미기

[지킬 공식문서](https://jekyllrb.com/docs/themes/)


## Jekyll 테마 고르기

아래 네곳에서 Jekyll 테마를 선택 가능

- [jamstackthemes.dev](https://jamstackthemes.dev/ssg/jekyll/">jamstackthemes.dev)
- [jekyllthemes.org](http://jekyllthemes.org/">jekyllthemes.org)
- [jekyllthemes.io](https://jekyllthemes.io/">jekyllthemes.io)
- [themes.com](https://jekyll-themes.com/">jekyll-themes.com)

약 세번째 테마를 바꾸는 중인데 막상 골라놓고 나중에 보면 맘에 안들어서...

Fork 
    - [깔끔한 테마로 선택](https://github.com/goodstart57/tale)
Ref
    - [Header, OnLoadAction](https://jekyll-themes.com/derrick)

## Gem 기반 테마에 대하여

새로운 Jekyll 사이트를 생성하면 (jekyll new <PATH> 명령어를 이용하여) `Minima` 테마가 만들어진다.

- `jekyll new .` 명령어로 새로운 Jekyll 프로젝트 생성

```cmd
goods@DESKTOP-NG5QKVG MINGW64 /c/Workspace/jekyll_start
$ jekyll new .
Running bundle install in C:/Workspace/jekyll_start...
  Bundler: Fetching gem metadata from https://rubygems.org/...........
  Bundler: Fetching gem metadata from https://rubygems.org/.
  Bundler: Resolving dependencies...
  Bundler: Fetching public_suffix 4.0.3
  Bundler: Installing public_suffix 4.0.3
  Bundler: Using addressable 2.7.0
  Bundler: Using bundler 2.0.2
  Bundler: Using colorator 1.1.0
  Bundler: Using concurrent-ruby 1.1.5
  Bundler: Using eventmachine 1.2.7 (x64-mingw32)
  Bundler: Using http_parser.rb 0.6.0
  Bundler: Using em-websocket 0.5.1
  Bundler: Fetching ffi 1.12.1 (x64-mingw32)
  Bundler: Installing ffi 1.12.1 (x64-mingw32)
  Bundler: Using forwardable-extended 2.6.0
  Bundler: Fetching i18n 1.8.2
  Bundler: Installing i18n 1.8.2
  Bundler: Using sassc 2.2.1 (x64-mingw32)
  Bundler: Using jekyll-sass-converter 2.0.1
  Bundler: Using rb-fsevent 0.10.3
  Bundler: Fetching rb-inotify 0.10.1
  Bundler: Installing rb-inotify 0.10.1
  Bundler: Fetching listen 3.2.1
  Bundler: Installing listen 3.2.1
  Bundler: Using jekyll-watch 2.2.1
  Bundler: Using kramdown 2.1.0
  Bundler: Using kramdown-parser-gfm 1.1.0
  Bundler: Using liquid 4.0.3
  Bundler: Using mercenary 0.3.6
  Bundler: Using pathutil 0.16.2
  Bundler: Fetching rouge 3.15.0
  Bundler: Installing rouge 3.15.0
  Bundler: Using safe_yaml 1.0.5
  Bundler: Fetching unicode-display_width 1.6.1
  Bundler: Installing unicode-display_width 1.6.1
  Bundler: Using terminal-table 1.8.0
  Bundler: Using jekyll 4.0.0
  Bundler: Using jekyll-feed 0.13.0
  Bundler: Using jekyll-seo-tag 2.6.1
  Bundler: Using minima 2.5.1
  Bundler: Using thread_safe 0.3.6
  Bundler: Fetching tzinfo 1.2.6
  Bundler: Installing tzinfo 1.2.6
  Bundler: Using tzinfo-data 1.2019.3
  Bundler: Using wdm 0.1.1
  Bundler: Bundle complete! 6 Gemfile dependencies, 34 gems now installed.
  Bundler: Use `bundle info [gemname]` to see where a bundled gem is installed.
  Bundler: Post-install message from i18n:
  Bundler:
  Bundler: HEADS UP! i18n 1.1 changed fallbacks to exclude default locale.
  Bundler: But that may break your application.
  Bundler:
  Bundler: If you are upgrading your Rails application from an older version of Rails:
  Bundler:
  Bundler: Please check your Rails app for 'config.i18n.fallbacks = true'.
  Bundler: If you're using I18n (>= 1.1.0) and Rails (< 5.2.2), this should be
  Bundler: 'config.i18n.fallbacks = [I18n.default_locale]'.
  Bundler: If not, fallbacks will be broken in your app by I18n 1.1.x.
  Bundler:
  Bundler: If you are starting a NEW Rails application, you can ignore this notice.
  Bundler:
  Bundler: For more info see:
  Bundler: https://github.com/svenfuchs/i18n/releases/tag/v1.1.0
New jekyll site installed in C:/Workspace/jekyll_start.
```

### 초기 생성된 파일/폴더

```directory
jekyll_start
    ├─ _posts
        └─ 2020-01-23-welcome-to-jekyll.markdown

    ├─ _config.yml
    ├─ .gitignore
    ├─ 404.html
    ├─ about.markdown
    ├─ Gemfile
    ├─ Gemfile.lock
    └─ index.markdown
```

>
> `Gemfile`, `Gemfile.lock` : Jekyll 사이트를 빌드하기 위해 `bundler`가 설치가 필요한 Gem이나 Gem의 버전을 관리하는 용도
>
> `_config.yml` : Jekyll 사이트 환경설정 파일
>

>
> theme gem이 있다면 `bundle update` 혹은 `bundle update <THEME>`을 통해서 프로젝트의 모든 Gem을 업데이트 할 수 있다.
> 


### 기본 테마 덮어쓰기 (Overriding theme defaults)

1. 기존 `_layouts\`와 `_includes\`의 내용 백업

2. `bundle info --path`를 이용하여 설치한 theme의 경로를 찾고 열기

```cmd
$ bundle info --path minima
C:/Ruby26-x64/lib/ruby/gems/2.6.0/gems/minima-2.5.1

$ cd C:/Ruby26-x64/lib/ruby/gems/2.6.0/gems/minima-2.5.1
$ TREE /F
minima-2.5.1
│  LICENSE.txt
│  README.md
│
├─assets
│      main.scss
│      minima-social-icons.svg
│
├─_includes
│      disqus_comments.html
│      footer.html
│      google-analytics.html
│      head.html
│      header.html
│      icon-github.html
│      icon-github.svg
│      icon-twitter.html
│      icon-twitter.svg
│      social.html
│
├─_layouts
│      default.html
│      home.html
│      page.html
│      post.html
│
└─_sass
    │  minima.scss
    │
    └─minima
            _base.scss
            _layout.scss
            _syntax-highlighting.scss
```
- 해당 Directory Tree는 minima 테마의 것으로 새로 생성한 `jekyll_start` 프로젝트에 `_include/footer.html`을 생성하면 **내가 원하는 footer를 사용할 수 있다.**

- `jekyll_start` 프로젝트에서 minima 테마를 적용하는 부분은 `_config.yml`의 `theme` 부분

3. 