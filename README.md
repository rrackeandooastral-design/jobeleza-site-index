# Jordânia Paz — site do estúdio

Site estático (HTML + CSS + JS puro). Sem build, sem dependências, sem framework.

## Estrutura

```
jobeleza-site/
├── index.html
├── assets/
│   ├── css/style.css
│   ├── js/app.js
│   └── img/            (8 fotos recortadas do Instagram)
├── tools/crop.py       (script que recorta os prints originais)
└── preview.png         (captura do resultado)
```

## Ver localmente

Duplo clique em `index.html` — funciona direto no navegador.

Ou, para simular servidor:

```powershell
cd C:\Users\clebe\jobeleza-site
python -m http.server 8080
```

Depois abra http://localhost:8080

## Publicar

**Vercel** (o mesmo que você já usa):

```powershell
cd C:\Users\clebe\jobeleza-site
npx vercel --prod
```

Ou arraste a pasta em https://vercel.com/new — sem configuração, é site estático.

**Netlify**: arraste a pasta em https://app.netlify.com/drop

## Paleta (mantida do site original)

| Token | Cor | Uso |
|---|---|---|
| `--pink` | `#ff2e93` | destaque principal |
| `--pink-deep` | `#d81b7a` | gradientes |
| `--pink-soft` | `#ffb3d9` | textos de apoio |
| `--plum-3` | `#2a0a1c` | cards |
| `--plum` | `#14050e` | fundo de seção |
| `--ink` | `#0b0408` | fundo geral |
| `--cream` | `#fdf4f8` | texto |
| `--wa` | `#25d366` | WhatsApp |

Tipografia: **Montserrat** (texto) + **Great Vibes** (destaques manuscritos).

## Dados reais usados

- WhatsApp: (62) 99190-1136 → `wa.me/5562991901136`
- Instagram: `@jobelezae.saude`
- Local: Parque Amazônia, Goiás
- Serviços: massagem modeladora, relaxante, banho de lua, depilação a cera, estética capilar e corporal

**Nada foi inventado**: sem preços, sem horários, sem depoimentos falsos, sem "anos de experiência".

## Recortar imagens de novo

Se quiser trocar/adicionar fotos, edite a lista `JOBS` em `tools/crop.py`
(caminho do print + nome final + caixa de recorte) e rode:

```powershell
python tools/crop.py
```

## Pendências

1. **Fotos em alta**: as atuais vêm de prints (591px de largura). Para hero e
   seção "Sobre", o ideal é pedir os originais em alta resolução.
2. **Endereço completo**: hoje só a região. Se quiser o endereço no site,
   é só me passar.
3. **Preços**: se quiser exibir valores, preciso dos valores reais.
4. **Google Meu Negócio / mapa**: posso embutir um mapa quando houver endereço.
