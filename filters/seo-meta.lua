-- seo-meta.lua
-- Inject per-page <link rel="canonical">, og:url, and og:type into the HTML <head>.
-- Quarto does not emit these by default; they all require the page's own URL, which we
-- derive from the site-url plus the input file's path relative to the project root.

local SITE_URL = "https://mauricio-romero.com"

local function normalize(p)
  return (p:gsub("\\", "/"))
end

local function is_absolute(p)
  return p:match("^%a:[/\\]") ~= nil or p:match("^/") ~= nil
end

-- Path of `file` relative to project `base`, robust to absolute/relative inputs.
local function relpath(file, base)
  file = normalize(file)
  base = normalize(base)
  if base ~= "" then
    if base:sub(-1) ~= "/" then base = base .. "/" end
    if file:sub(1, #base) == base then
      return file:sub(#base + 1)
    end
  end
  if is_absolute(file) then
    return file:match("[^/]+$") or file
  end
  return file  -- already relative to the project root
end

function Pandoc(doc)
  -- HTML website pages only (skip non-HTML outputs).
  if not quarto.doc.is_format("html:js") then
    return doc
  end

  local rel = relpath(quarto.doc.input_file or "", quarto.project.directory or "")
  rel = rel:gsub("%.qmd$", ".html"):gsub("%.md$", ".html")

  local is_home = (rel == "index.html")

  -- Bare-directory canonical: index.html -> "", foo.html -> "foo.html".
  local canon_path = rel:gsub("index%.html$", "")
  local url = SITE_URL .. "/" .. canon_path
  url = url:gsub("([^:])//+", "%1/")  -- collapse accidental double slashes

  local og_type = is_home and "profile" or "website"

  local header = string.format(
    '<link rel="canonical" href="%s">\n' ..
    '<meta property="og:url" content="%s">\n' ..
    '<meta property="og:type" content="%s">',
    url, url, og_type)

  quarto.doc.include_text("in-header", header)
  return doc
end
