FROM node:22-alpine AS builder

RUN apk add --no-cache --repository=https://dl-cdn.alpinelinux.org/alpine/edge/community hugo

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm ci --ignore-scripts

COPY . .
ENV HUGO_ENABLEGITINFO=false
RUN npm run build:css && hugo --minify --gc

FROM caddy:2-alpine

COPY Caddyfile /etc/caddy/Caddyfile
COPY --from=builder /app/public /srv

EXPOSE 80
