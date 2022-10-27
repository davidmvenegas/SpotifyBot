const CLIENT_ID = '4571820e8fd04623b66368f248ba2ef5'
const CLIENT_SECRET = '11703fba422642a5a1a7259a9ac446e3'

const getToken = async () => {
    const result = await fetch('https://accounts.spotify.com/api/token', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic ' + btoa(CLIENT_ID + ':' + CLIENT_SECRET)
        },
        body: 'grant_type=client_credentials'
    })

    const data = await result.json()
    const token = data.access_token
    return token
}

const getShows = async (token) => {
    console.log(token)
    const result = await fetch(`https://api.spotify.com/v1/me/shows?limit=50`, {
        method: 'GET',
        headers: { 'Authorization': 'Bearer ' + token }
    });

    const data = await result.json();
    console.log(data)
}

getToken().then(token => getShows(token))