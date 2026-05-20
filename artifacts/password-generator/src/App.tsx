import { useState, useCallback } from "react";

const UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const LOWERCASE = "abcdefghijklmnopqrstuvwxyz";
const DIGITS = "0123456789";
const SYMBOLS = "!@#$%^&*()_+-=[]{}|;:,.<>?";

function generatePassword(
  length: number,
  useUppercase: boolean,
  useLowercase: boolean,
  useDigits: boolean,
  useSymbols: boolean
): string {
  let charset = "";
  const guaranteed: string[] = [];

  if (useUppercase) { charset += UPPERCASE; guaranteed.push(UPPERCASE[Math.floor(Math.random() * UPPERCASE.length)]); }
  if (useLowercase) { charset += LOWERCASE; guaranteed.push(LOWERCASE[Math.floor(Math.random() * LOWERCASE.length)]); }
  if (useDigits) { charset += DIGITS; guaranteed.push(DIGITS[Math.floor(Math.random() * DIGITS.length)]); }
  if (useSymbols) { charset += SYMBOLS; guaranteed.push(SYMBOLS[Math.floor(Math.random() * SYMBOLS.length)]); }

  if (!charset) return "";

  const remaining = Array.from({ length: length - guaranteed.length }, () =>
    charset[Math.floor(Math.random() * charset.length)]
  );

  const all = [...guaranteed, ...remaining];
  for (let i = all.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [all[i], all[j]] = [all[j], all[i]];
  }
  return all.join("");
}

function strengthLabel(password: string, options: { upper: boolean; lower: boolean; digits: boolean; symbols: boolean }): { label: string; color: string; width: string } {
  if (!password) return { label: "", color: "", width: "0%" };
  let score = 0;
  if (password.length >= 8) score++;
  if (password.length >= 12) score++;
  if (password.length >= 16) score++;
  if (options.upper && options.lower) score++;
  if (options.digits) score++;
  if (options.symbols) score++;

  if (score <= 2) return { label: "Weak", color: "#ef4444", width: "25%" };
  if (score <= 3) return { label: "Fair", color: "#f97316", width: "50%" };
  if (score <= 4) return { label: "Good", color: "#eab308", width: "75%" };
  return { label: "Strong", color: "#22c55e", width: "100%" };
}

export default function App() {
  const [length, setLength] = useState(16);
  const [useUppercase, setUseUppercase] = useState(true);
  const [useLowercase, setUseLowercase] = useState(true);
  const [useDigits, setUseDigits] = useState(true);
  const [useSymbols, setUseSymbols] = useState(true);
  const [password, setPassword] = useState("");
  const [copied, setCopied] = useState(false);

  const noneSelected = !useUppercase && !useLowercase && !useDigits && !useSymbols;

  const generate = useCallback(() => {
    if (noneSelected) return;
    const pw = generatePassword(length, useUppercase, useLowercase, useDigits, useSymbols);
    setPassword(pw);
    setCopied(false);
  }, [length, useUppercase, useLowercase, useDigits, useSymbols, noneSelected]);

  const copy = () => {
    if (!password) return;
    navigator.clipboard.writeText(password).then(() => {
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    });
  };

  const strength = strengthLabel(password, { upper: useUppercase, lower: useLowercase, digits: useDigits, symbols: useSymbols });

  return (
    <div className="app-bg">
      <div className="card">
        <div className="card-header">
          <div className="lock-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <rect x="3" y="11" width="18" height="11" rx="2" ry="2" />
              <path d="M7 11V7a5 5 0 0 1 10 0v4" />
            </svg>
          </div>
          <h1>Password Generator</h1>
          <p className="subtitle">Create a secure, random password</p>
        </div>

        <div className="output-box">
          <span className={`password-text ${!password ? "placeholder" : ""}`}>
            {password || "Click Generate to create a password"}
          </span>
          <button
            className={`copy-btn ${copied ? "copied" : ""}`}
            onClick={copy}
            disabled={!password}
            title="Copy to clipboard"
          >
            {copied ? (
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
                <polyline points="20 6 9 17 4 12" />
              </svg>
            ) : (
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                <rect x="9" y="9" width="13" height="13" rx="2" ry="2" />
                <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1" />
              </svg>
            )}
          </button>
        </div>

        {password && (
          <div className="strength-bar-wrap">
            <div className="strength-track">
              <div
                className="strength-fill"
                style={{ width: strength.width, background: strength.color }}
              />
            </div>
            <span className="strength-label" style={{ color: strength.color }}>
              {strength.label}
            </span>
          </div>
        )}

        <div className="section">
          <div className="section-header">
            <span className="section-label">Password Length</span>
            <span className="length-badge">{length}</span>
          </div>
          <input
            type="range"
            min={4}
            max={64}
            value={length}
            onChange={(e) => setLength(Number(e.target.value))}
            className="slider"
          />
          <div className="slider-ticks">
            <span>4</span><span>16</span><span>32</span><span>64</span>
          </div>
        </div>

        <div className="section">
          <div className="section-label">Character Types</div>
          <div className="options-grid">
            {[
              { label: "Uppercase", sublabel: "A–Z", value: useUppercase, set: setUseUppercase },
              { label: "Lowercase", sublabel: "a–z", value: useLowercase, set: setUseLowercase },
              { label: "Numbers", sublabel: "0–9", value: useDigits, set: setUseDigits },
              { label: "Symbols", sublabel: "!@#$…", value: useSymbols, set: setUseSymbols },
            ].map(({ label, sublabel, value, set }) => (
              <button
                key={label}
                className={`option-chip ${value ? "active" : ""}`}
                onClick={() => set(!value)}
              >
                <span className="chip-label">{label}</span>
                <span className="chip-sub">{sublabel}</span>
              </button>
            ))}
          </div>
          {noneSelected && (
            <p className="warning">Select at least one character type</p>
          )}
        </div>

        <button
          className="generate-btn"
          onClick={generate}
          disabled={noneSelected}
        >
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
            <polyline points="1 4 1 10 7 10" />
            <polyline points="23 20 23 14 17 14" />
            <path d="M20.49 9A9 9 0 0 0 5.64 5.64L1 10m22 4-4.64 4.36A9 9 0 0 1 3.51 15" />
          </svg>
          Generate Password
        </button>

        {copied && (
          <p className="copied-toast">Copied to clipboard!</p>
        )}
      </div>
    </div>
  );
}
