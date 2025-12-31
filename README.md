# 🐦 Backend – Micro réseau social (geek / humour / culture)

Backend d’un micro réseau social type Twitter, centré sur la culture geek, l’humour et le partage léger.  
Le projet met l’accent sur la **performance du feed**, la **simplicité produit**, et une **modération stricte** (pas de politique, pas de haine, pas de religion).

## 🎯 Objectif

Créer une plateforme :
- fluide (scroll instantané, faible latence),
- saine (pas de débats toxiques),
- simple (features limitées mais bien exécutées),
- scalable.

## 🚀 Stack technique

- **Framework** : Django
- **API** : Strawberry GraphQL (persisted queries)
- **Base de données** : PostgreSQL
- **Cache / rate limit / broker** : Redis
- **Workers async** : Celery ou Dramatiq
- **Stockage médias** : S3 / R2 / MinIO
- **Reverse proxy** : Nginx ou Caddy

## 🧱 Principes d’architecture

- Feed optimisé :
  - pagination **keyset** (pas d’OFFSET)
  - cache Redis par user + curseur
- Tout ce qui est lent est asynchrone :
  - modération
  - thumbnails
  - fan-out (si activé plus tard)
- Pas de N+1 :
  - dataloaders
  - prefetch / select_related
- Pas de requêtes GraphQL libres en prod :
  - uniquement des **persisted queries**

## 📦 Périmètre MVP

Voir `docs/mvp_scope.md`

Résumé :
- Auth, profils, posts texte + image
- Home feed (following), profile feed
- Follow / like
- Modération minimale + admin

Pas de :
- reposts, DMs, trending, politique, religion, haine

## 🛡 Modération

Voir `docs/moderation_policy.md`

Trois niveaux :
1. Hors thème (politique / religion) → soft-hide
2. Haine / abus → suppression + sanction
3. Zone grise → flag + review

## ⚡ Performance

Voir `docs/perf_rules.md`

Objectifs :
- p95 home feed < 300 ms
- scroll fluide même à forte charge
- 0 requête SQL > 100 ms

## 🗂 Structure du repo

```
.
├── backend/
├── docs/
│   ├── architecture.md
│   ├── mvp_scope.md
│   ├── moderation_policy.md
│   └── perf_rules.md
└── README.md
```

## 🛠 Setup (local)

```bash
docker-compose up --build
python manage.py migrate
python manage.py createsuperuser
```

## 📈 Roadmap

Voir le PDF de roadmap ou les issues GitHub.

## 🤝 Contribuer

- Pas de feature hors périmètre sans discussion
- Toute nouvelle feature doit respecter :
  - performance
  - simplicité
  - esprit du produit (chill / fun / safe)

## 🧠 Philosophie

> *“Ce n’est pas un réseau social pour convaincre, c’est un réseau social pour respirer.”*
