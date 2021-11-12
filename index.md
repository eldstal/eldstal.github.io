---
pagetitle: Albin Eldstål-Ahrens

...


# Links

# Software

## Security

### [strinvader](https://github.com/eldstal/strinvader"), a unicode denormalizer

Unicode is quite complex. Since there are many different ways to encode the same text,
applications may use _normalization_ to preprocess text. Strinvader is a tool to
find multiple text inputs which normalize to the same (given) text. This is useful in
security research, because sometimes security features such as block lists are applied
to text _before_ normalization. When attacking such an application, strinvader
can generate a text encoding such as `www.exAｍᵖ𝑙𝑒.com` which will pass the blocklist
and be normalized to `www.example.com` before being used.

## Other


### [Cardcinogen](https://github.com/eldstal/cardcinogen), a deck generator for [Tabletop Simulator](https://store.steampowered.com/app/286160/Tabletop_Simulator/)

Cardcinogen is a templating system which allows you to create styles for playing cards and
populate those cards with content from your own data. This is useful to make expansions
for card-based games such as Concept or Fluxx.
