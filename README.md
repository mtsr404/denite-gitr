# denite-gitr

denite.nvim source for git diff.

## Requirements

- Neovim
- denite.nvim
- Gina

## Usage
```vim
:Denite git_diffs:diff_target " branch or commit hash
```

### Example
```vim
nmap <Space>gD :Denite git_diffs:master -winheight=10 -split=horizontal -mode=insert -buffer-name=difffiles -post-action=open<CR>
nmap <Space>gr :Denite -resume -winheight=20 -split=horizontal -mode=insert -buffer-name=difffiles<CR>
nmap <Space>gn :Denite -resume -refresh -cursor-pos=+1 -immediately -buffer-name=difffiles<CR>
nmap <Space>gp :Denite -resume -refresh -cursor-pos=-1 -immediately -buffer-name=difffiles<CR>
```
