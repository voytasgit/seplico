# Windows / GitHub setup

This guide keeps the first public Seplico publication deliberate. Do not publish the repository until the license, publication metadata and any patent question have been checked.

## 1. Prepare the local repository

Open PowerShell:

```powershell
cd C:\_github
New-Item -ItemType Directory -Path seplico -Force | Out-Null
```

Extract the contents of the release ZIP directly into `C:\_github\seplico` so that `README.md` is directly inside that directory.

Then:

```powershell
cd C:\_github\seplico
git init
git branch -M main
git status
```

## 2. Verify before the first commit

With Python installed:

```powershell
py -m pip install -r requirements-dev.txt
py -m unittest discover -s tests -v
```

All tests must pass.

Review at least:

```text
README.md
SPECIFICATION.md
AUTHORS.md
NOTICE
CITATION.cff
LICENSE
PUBLISHING.md
```

## 3. Create the local first commit

Configure your real Git author identity if needed:

```powershell
git config user.name "Vadym Voytas"
git config user.email "YOUR-GITHUB-EMAIL"
```

Then:

```powershell
git add .
git status
git commit -m "Initial Seplico specification draft"
```

Do not backdate the commit.

## 4. Create GitHub repository privately first

Create an empty repository named `seplico` under your GitHub account. Prefer **Private** while performing the final checks. Do not initialize it with a README, license or `.gitignore`, because those files already exist locally.

Connect it:

```powershell
git remote add origin https://github.com/voytasgit/seplico.git
git push -u origin main
```

Now replace placeholder/canonical repository metadata only after the final GitHub URL is known. Commit those metadata changes while the repository is still private.

## 5. Publication day

On the actual publication day:

1. run the test suite again;
2. confirm that no personal/test data accidentally identifies a real applicant;
3. update the actual first-publication date in `AUTHORS.md` and `CITATION.cff`;
4. commit and push that metadata update;
5. enable GitHub immutable releases before publishing the first release;
6. make the repository public;
7. create and publish the first release/tag from the exact reviewed commit;
8. connect the public repository to Zenodo and archive the release;
9. record the DOI in the next metadata update.

The repository publication and first release should ideally happen on the same calendar day so the public provenance story stays simple.

## 6. Suggested first public tag

The current package is intentionally a draft. A reasonable first public tag is:

```text
v0.2.0-draft
```

If you decide that the first public version should be less mature, rename it consistently before publication rather than rewriting history afterward.
