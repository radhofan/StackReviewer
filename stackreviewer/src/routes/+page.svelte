<script>  
    // Define lists of popular frontend, backend, and database frameworks  
    const frontendFrameworks = ['React', 'Vue', 'Angular', 'Svelte', 'Ember'];  
    const backendFrameworks = ['NestJS', 'Express', 'Django', 'Flask', 'Spring Boot'];  
    const databaseFrameworks = ['MySQL', 'PostgreSQL', 'MongoDB', 'SQLite', 'Oracle'];  
    
    // State variables to store selected frontend, backend, and database frameworks  
    let selectedFrontend = '';  
    let selectedBackend = '';  
    let selectedDatabase = '';  
    
    // State variable to store generated data  
    let generatedData = null;  
    
    // Function to reset selections  
    function resetSelections() {  
        selectedFrontend = '';  
        selectedBackend = '';  
        selectedDatabase = '';  
        generatedData = null;  
    }  
    
    // Function to generate tech stack info  
    async function generateTechStackInfo() {  
        if (selectedFrontend && selectedBackend && selectedDatabase) {  
        const response = await fetch('http://127.0.0.1:5000/generate', {  
            method: 'POST',  
            headers: {  
            'Content-Type': 'application/json',  
            },  
            body: JSON.stringify({  
            frontend: selectedFrontend,  
            backend: selectedBackend,  
            database: selectedDatabase,  
            }),  
        });  
    
        const data = await response.json();  
        generatedData = data;  
        }  
    }  
    </script>  
        
        
    <div class="flex flex-col items-center justify-center min-h-screen bg-gray-100">  
        <div class="bg-white p-6 rounded-lg shadow-md text-center w-full max-w-md">  
            <h1 class="text-2xl font-bold mb-6">Tech Stack Reviewer</h1>  
    
            <div>  
            <h2 class="text-lg font-semibold mb-2">Choose Frontend Framework</h2>  
            <ul class="space-y-2">  
                {#each frontendFrameworks as framework}  
                <li>  
                    <label class="flex items-center">  
                    <input type="radio" bind:group={selectedFrontend} value={framework} class="mr-2" />  
                    {framework}  
                    </label>  
                </li>  
                {/each}  
            </ul>  
            </div>  
    
            <div class="mt-6">  
            <h2 class="text-lg font-semibold mb-2">Choose Backend Framework</h2>  
            <ul class="space-y-2">  
                {#each backendFrameworks as framework}  
                <li>  
                    <label class="flex items-center">  
                    <input type="radio" bind:group={selectedBackend} value={framework} class="mr-2" />  
                    {framework}  
                    </label>  
                </li>  
                {/each}  
            </ul>  
            </div>  
    
            <div class="mt-6">  
            <h2 class="text-lg font-semibold mb-2">Choose Database</h2>  
            <ul class="space-y-2">  
                {#each databaseFrameworks as framework}  
                <li>  
                    <label class="flex items-center">  
                    <input type="radio" bind:group={selectedDatabase} value={framework} class="mr-2" />  
                    {framework}  
                    </label>  
                </li>  
                {/each}  
            </ul>  
            </div>  
    
            {#if selectedFrontend && selectedBackend && selectedDatabase}  
            <button class="mt-6 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600" on:click={generateTechStackInfo}>Generate Insights</button>  
            {/if}  
    
            {#if generatedData}  
            <div class="mt-6">  
                <h3 class="text-xl font-bold mb-2">Generated Insights:</h3>  
                <p class="font-semibold">Pros: {generatedData.pros}</p>  
                <p class="font-semibold">Cons: {generatedData.cons}</p>  
                <p class="font-semibold">Summary: {generatedData.summary}</p>  
            </div>  
            {/if}  
    
            <button class="mt-6 px-4 py-2 bg-red-500 text-white rounded hover:bg-red-600" on:click={resetSelections}>Reset Selections</button>  
        </div>  
    </div>  