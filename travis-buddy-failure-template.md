## Travis Buddy
Hey **{{author}}**,
We spotted the following mistakes in your code

{{#jobs}}
{{#scripts}}
<details>
  <summary>
    <strong>
     {{command}}
    </strong>
  </summary>

```
{{&contents}}
```
</details>
<br />
{{/scripts}}
{{/jobs}
