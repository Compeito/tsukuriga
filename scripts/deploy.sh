#!/bin/sh

cd `dirname $0`/../

alias docker-compose-prod='docker-compose -f docker-compose.yml -f docker-compose.prod.yml'
docker-compose-prod down

# イメージの再ビルド
docker-compose-prod build

# 依存関係の更新とDBマイグレーション
docker-compose-prod run web bash -c "poetry install --no-dev --no-root && python manage.py migrate"

# js/cssの再ビルドと配置
rm -rf nginx/assets/bundles/*
rm -rf nginx/assets/webpack-stats.json
docker-compose-prod run node bash -c "yarn && yarn run build"
docker-compose-prod run web python manage.py collectstatic --no-input

docker-compose-prod up -d
