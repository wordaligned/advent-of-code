#! /usr/bin/env bash
grep -E "(..).*\1" - | grep -cE "(.).\1"
