

## Running from tmuxinator

```yml
name: cp_ladder
root: ~/works/
# This environment variable is used for neovim configuration 
# (this ensures that opening html file is for django template)
# See https://github.com/malkoG/dotfiles/blob/main/private_dot_config/nvim/after/ftplugin/html.lua
pre_window: export USING_DJANGO_TEMPLATE=yes 
windows:
  - editor:
      layout: main-vertical
      panes:
        - cd ./cp-ladder/ && poetry shell
  - frontend:
      layout: main-vertical
      panes:
        - cd ./cp-ladder/ 
  - debugging:
      layout: main-vertical
      panes:
        - cd ./cp-ladder/ && poetry run python manage.py runserver
        - cd ./cp-ladder/ && poetry run python manage.py tailwind start
```
