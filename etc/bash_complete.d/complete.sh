#!/bin/bash

_tool_subcommand(){
    command=${COMP_WORDS[$COMP_CWORD]}
    COMPREPLY=( `compgen -W "sample" $command` ) 
}

_tool_subcommands(){
    command=${COMP_WORDS[1]} 
    cur_word=${COMP_WORDS[$COMP_CWORD]}
    case $command in
        'sample')
            ######################################
            # if arg num > 2  return
            #
            if [ $COMP_CWORD -gt 2 ]; then
                return
            fi
            _tool_sample $cur_word;;
    esac
}

_tool_sample(){
    opt_word=$1
    opt_len=${#opt_word}
    COMPREPLY=( `compgen -W "--foo --bar" -- $1` )
}

_tool(){
    COMPREPLY=()

    if [ $COMP_CWORD -eq 1 ]; then
        _tool_subcommand 
    elif [ $COMP_CWORD -ge 2 ]; then
        _tool_subcommands
    fi
}

complete -F _tool tool
