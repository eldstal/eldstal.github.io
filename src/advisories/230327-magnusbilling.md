---
pagetitle: CVE-2023-30258 Security advisory

...

## Security advisory

A command injection vulnerability exists in magnusbilling versions 6 and 7. The vulnerability allows an unauthenticated user to execute arbitrary OS commands on the host, with the privileges of the web server.

### Affected products
magnusbilling 7 up to and including commit [7af21ed620](https://github.com/magnussolution/magnusbilling7/commit/7af21ed6203f80947a5df4a92df0be7a6aa158f9)

magnusbilling 6 (all versions)

### Steps to reproduce

The following proof of concept uses a harmless `sleep 30` command as a payload.

1. Visit `/mbilling/lib/icepay/icepay.php?democ=/dev/null;sleep%2030;ls%20a`
2. Observe that the page takes 30 seconds to load
3. Visit `/mbilling/lib/icepay/icepay.php?democ=/dev/null;sleep%203;ls%20a`
4. Observe that the page takes only 3 seconds to load

### Cause

A piece of demonstration code is present in `lib/icepay/icepay.php`, with a call to `exec()` at [line 753](https://github.com/magnussolution/magnusbilling7/blob/f6cd038161349895ff6f186405b9a89f564c9448/lib/icepay/icepay.php#L753). The parameter to `exec()` includes the GET parameter `democ`, which is controlled by the user.

### Impact

An unauthenticated user is able to execute arbitrary OS commands. The commands run with the privileges of the web server process, typically `www-data`. At a minimum, this allows an attacker to compromise the billing system and its database.

### Proposed Mitigation

Remove the demo code from `icepay.php`.


### History
- 2023-06-26: CVE-2023-30258 assigned
- 2023-03-28: Initial report removed by maintainer
- 2023-03-27: Vulnerability [fixed](https://github.com/magnussolution/magnusbilling7/commit/ccff9f6370f530cc41ef7de2e31d7590a0fdb8c3)
- 2023-03-27: Vulnerability [reported](https://github.com/magnussolution/magnusbilling7/issues/627)
