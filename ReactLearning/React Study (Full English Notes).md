## React Study (Full English Notes)

### 1. Entry

#### 1.1 Preparation

![image-20240801080929422](ReactLearning/React Study (Full English Notes).assets/image-20240801080929422.png)

In Pycharm, create stuff with React as its frame (here names it tccdog) Soon it will create relevant documents automatically

#### 1.2 Experiment

![image-20240801081704451](./React Study (Full English Notes).assets/image-20240801081704451.png)

click and run this program, showing this page down below means a successful installment

![image-20240801081744470](./React Study (Full English Notes).assets/image-20240801081744470.png)

### 2 First React Application

#### 2.1 Hello TCCDOG

```python
export default function App(){
  return <div>Hello TCCDOG</div>
}
```

Open the page and see Hello TCCDOG immediately.

#### 2.2 import css

If you need to use either local or online css like how you do it in HTML, then just type

```react
import './UrPath/fileName.css'
```

#### 2.3 Advanced Label and Prompts

If you need to set a elements' class name, then you should do like this:

##### 1.className

```react
return <form className='tccdog'>

</form>
```

##### 2.label & htmlFor & imput

```react
function MyForm() { 
    return (
        <form>
            <label htmlFor="username">Username:</label>      
            <input type="text" id="username" name="username" />       
            <label htmlFor="password">Password:</label>      
            <input type="password" id="password" name="password" />       
            <button type="submit">Submit</button>    </form>  ); }
```

usually label is used with 'input'

**`<label htmlFor="username">Username:</label>`**:

- `htmlFor="username"` means this label is related to `id="username"` 's input box,
  - When clicking “Username:” label，cursor automatically goes to `id="username"` 's input box.

**`<input type="text" id="username" name="username" />`**:

- This box's`id` is `username`，aligns with`label` 's' `htmlFor`.

  ![image-20240801083437292](./React Study (Full English Notes).assets/image-20240801083437292.png)

##### 3. IMPORTANT only one root is permitted in return

If you are adding more than one root in return, it will display error msg. It is like:

```react
<form>xxxxx
	<div></div>
</form>
<h1>xxxxxxx</h1>
```

So if you want to add more than 1 root in return, then you should do like this:

<>

<form>xxxxx
	<div></div>
</form>
<h1>xxxxxxx</h1>

</>

<></> are called fragments



