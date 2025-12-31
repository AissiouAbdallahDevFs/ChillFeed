# Règles de performance

## Feed
- Keyset pagination uniquement
- Cache Redis par user + curseur
- TTL court (30–120s)

## API
- Pas de N+1 queries
- Dataloaders / select_related / prefetch_related
- Rate limiting Redis

## Async
- Modération
- Thumbnails
- Fan-out futur

## Objectifs
- p95 feed < 300ms
- 0 requête SQL > 100ms
