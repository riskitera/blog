---
title: "{{ replace .File.ContentBaseName "-" " " | title }}"
description: ""
slug: "{{ .File.ContentBaseName }}"
date: {{ .Date }}
draft: true
translationKey: "{{ .File.ContentBaseName }}"
---
