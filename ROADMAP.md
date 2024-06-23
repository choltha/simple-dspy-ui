# Roadmap

## Prototype

### MVP
Setup Gradio locally. Implement fewshot:
- Meta description of what to do (Signature)
- At least one example of how to do it (input / output)
- Resulting Prompt for copy/paste to other tools
- API Key input field
- Backend: Target Model is gpt-3.5-turbo, judge is gpt-4o


### simple optimizer scenario
- what optimizer can i use? would love to: 
  - user gives prompt. generate examples based on generations. Use those for bootstrap/test split, then run real optimizer. User can bring their own dataset if they want to
  - how do do metric???
  - ...


## resources
### diff view
https://www.gradio.app/playground?demo=Diff_Texts&code=ZnJvbSBkaWZmbGliIGltcG9ydCBEaWZmZXIKCmltcG9ydCBncmFkaW8gYXMgZ3IKCgpkZWYgZGlmZl90ZXh0cyh0ZXh0MSwgdGV4dDIpOgogICAgZCA9IERpZmZlcigpCiAgICByZXR1cm4gWwogICAgICAgICh0b2tlblsyOl0sIHRva2VuWzBdIGlmIHRva2VuWzBdICE9ICIgIiBlbHNlIE5vbmUpCiAgICAgICAgZm9yIHRva2VuIGluIGQuY29tcGFyZSh0ZXh0MSwgdGV4dDIpCiAgICBdCgoKZGVtbyA9IGdyLkludGVyZmFjZSgKICAgIGRpZmZfdGV4dHMsCiAgICBbCiAgICAgICAgZ3IuVGV4dGJveCgKICAgICAgICAgICAgbGFiZWw9IlRleHQgMSIsCiAgICAgICAgICAgIGluZm89IkluaXRpYWwgdGV4dCIsCiAgICAgICAgICAgIGxpbmVzPTMsCiAgICAgICAgICAgIHZhbHVlPSJUaGUgcXVpY2sgYnJvd24gZm94IGp1bXBlZCBvdmVyIHRoZSBsYXp5IGRvZ3MuIiwKICAgICAgICApLAogICAgICAgIGdyLlRleHRib3goCiAgICAgICAgICAgIGxhYmVsPSJUZXh0IDIiLAogICAgICAgICAgICBpbmZvPSJUZXh0IHRvIGNvbXBhcmUiLAogICAgICAgICAgICBsaW5lcz0zLAogICAgICAgICAgICB2YWx1ZT0iVGhlIGZhc3QgYnJvd24gZm94IGp1bXBzIG92ZXIgbGF6eSBkb2dzLiIsCiAgICAgICAgKSwKICAgIF0sCiAgICBnci5IaWdobGlnaHRlZFRleHQoCiAgICAgICAgbGFiZWw9IkRpZmYiLAogICAgICAgIGNvbWJpbmVfYWRqYWNlbnQ9VHJ1ZSwKICAgICAgICBzaG93X2xlZ2VuZD1UcnVlLAogICAgICAgIGNvbG9yX21hcD17IisiOiAicmVkIiwgIi0iOiAiZ3JlZW4ifSksCiAgICB0aGVtZT1nci50aGVtZXMuQmFzZSgpCikKaWYgX19uYW1lX18gPT0gIl9fbWFpbl9fIjoKICAgIGRlbW8ubGF1bmNoKCkK


### arize - use via docker
see https://github.com/diicellman/dspy-gradio-rag/blob/main/compose.yml