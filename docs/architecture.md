# Architecture Backend — ChillFeed

## Vue d’ensemble

Architecture backend orientée performance et simplicité.

### Stack
- Django
- PostgreSQL
- Redis
- Workers async (Celery/Dramatiq)
- Docker Compose en local

### Principes
- Feed prioritaire
- Pagination keyset (jamais OFFSET)
- Cache Redis agressif
- Async pour tout ce qui est lent
- Séparation par apps Django

### Apps
- users : comptes et auth
- posts : contenus
- social : follows, likes
- moderation : reports, flags
- feeds : génération du feed (plus tard)
- media : gestion des images (plus tard)

### Flux principal
Client → API → Cache → DB → Workers (async)
