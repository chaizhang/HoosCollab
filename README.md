# HoosCollab

HoosCollab is a project management application (PMA) designed for university student organizations. Originally developed for a computer science class project. The site is now live on [Render](https://hooscollab.onrender.com), with PostgreSQL hosted via Supabase.

> **Note:** On first click Render may be asleep—please allow 30–60 seconds for the service to wake up.

Team Members: Chai Zhang, James Xu, Sanket Doddabendigere, Mila Ranocha, Michael Hijduk

## Overview
This repository contains the complete Django 5 codebase for HoosCollab. Users can create, organize, and manage tasks within groups such as homework teams, event committees, or hobby clubs. Core features include file uploads, in-task messaging, and role-based permissions.

## Tech Stack
- **Language & Framework:** Python 3 & Django 5  
- **Database:** PostgreSQL on Supabase
- **Authentication:** Google OAuth 2.0 (via `django-allauth`)  
- **File Storage:** Amazon S3 (via `django-storages`)  
- **CI/CD:** GitHub Actions, hosted on Render  
- **Version Control:** GitHub

## Features

### User Types & Roles 
- **Anonymous Visitor:** Can browse the list of organizations and view task titles, but no task details.
- **Common User:** Sign in via Google, create or join tasks, request or approve task membership, post messages, and upload and manage files.
- **PMA Administrator:** Granted site-wide moderation rights through the Django Admin; can view or delete any project, tasks, files, or messages.
- **Django Administrator:** Created with `createsuperuser`; has exclusive access to the default `/admin` interface for user and permission management.

### Organizations
Any user can create or join an organization. Anonymous visitors may view organization names and their associated tasks.

### Projects  
Projects group related tasks under a shared goal. Deleting a project also deletes all tasks within it.

### Tasks
Tasks are the core action items within a project. Each task includes:
- Name
- Due date
- Description
- Status
- Creation timestamp

Users can request to join tasks; project owners can approve or deny these requests. Each task includes an internal chat feed. Attachments (TXT, PDF, JPEG) can be uploaded for each task. Each file is tagged with metadata: title, description, keywords, uploader, and timestamp.

When a task is deleted, all related data—files, messages, user assignments, and join requests—are also removed.
