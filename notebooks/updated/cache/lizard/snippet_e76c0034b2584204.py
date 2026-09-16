def vim():
    install_package('vim')
    print_msg('## install ~/.vimrc\n')
    install_file_legacy('~/.vimrc')
    print_msg('\n## set up pathogen\n')
    run('mkdir -p  ~/.vim/autoload  ~/.vim/bundle')
    checkup_git_repo_legacy(url='https://github.com/tpope/vim-pathogen.git')
    run('ln -snf  ~/repos/vim-pathogen/autoload/pathogen.vim  ~/.vim/autoload/pathogen.vim'
        )
    print_msg('\n## install vim packages\n')
    install_package('ctags')
    repos = [{'name': 'vim-colors-solarized', 'url':
        'git://github.com/altercation/vim-colors-solarized.git'}, {'name':
        'nerdtree', 'url': 'https://github.com/scrooloose/nerdtree.git'}, {
        'name': 'vim-nerdtree-tabs', 'url':
        'https://github.com/jistr/vim-nerdtree-tabs.git'}, {'name':
        'tagbar', 'url': 'https://github.com/majutsushi/tagbar.git'}]
    checkup_git_repos_legacy(repos, base_dir='~/.vim/bundle')